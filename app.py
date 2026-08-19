import streamlit as st
from src.report_generator import generate_pdf_report
from src.sql_generator import generate_sql_query
        
from src.data_loader import load_data
from src.analyzer import (
    get_dataset_summary,
    get_statistics
)

from src.visualizer import (
    create_histogram,
    create_bar_chart,
    create_scatter_plot,
    create_box_plot,
    create_pie_chart,
    create_heatmap
)

from src.llm import get_llm
from src.insights import generate_insights

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# HEADER
# ==================================================

st.title("📊 AI Data Analyst")
st.markdown(
    "Upload a CSV or Excel file and explore your data with AI."
)

# ==================================================
# FILE UPLOADER
# ==================================================

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

# ==================================================
# MAIN APP
# ==================================================

if uploaded_file:

    try:

        # ==========================================
        # LOAD DATA
        # ==========================================

        df = load_data(uploaded_file)

        st.success("✅ File Loaded Successfully")
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview",
    "📈 Visualizations",
    "🧠 Insights",
    "🗄️ SQL Generator",
    "🤖 Chatbot"
])

        # ==========================================
        # DATA PREVIEW
        # ==========================================
        with tab1:

            st.subheader("📄 Dataset Preview")

            st.dataframe(
                df,
                use_container_width=True
            )

            # ==========================================
            # DATASET SUMMARY
            # ==========================================

            summary = get_dataset_summary(df)

            st.subheader("📌 Dataset Summary")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Rows",
                    summary["Rows"]
                )

            with col2:
                st.metric(
                    "Columns",
                    summary["Columns"]
                )

            with col3:
                st.metric(
                    "Missing Values",
                    df.isnull().sum().sum()
                )

            # ==========================================
            # COLUMN NAMES
            # ==========================================

            st.write("### Column Names")

            cols_text = ", ".join(
                summary["Column Names"]
            )

            st.info(cols_text)

            # ==========================================
            # MISSING VALUES
            # ==========================================

            st.subheader("⚠ Missing Values")

            import pandas as pd

            missing_df = pd.DataFrame(
                summary["Missing Values"].items(),
                columns=["Column", "Missing Values"]
            )

            st.dataframe(
                missing_df,
                use_container_width=True
            )

            # ==========================================
            # DATA TYPES
            # ==========================================

            st.subheader("🔤 Data Types")

            datatype_df = pd.DataFrame(
                summary["Data Types"].items(),
                columns=["Column", "Data Type"]
            )

            st.dataframe(
                datatype_df,
                use_container_width=True
            )

            # ==========================================
            # STATISTICAL SUMMARY
            # ==========================================

            st.subheader("📈 Statistical Summary")

            st.dataframe(
                get_statistics(df),
                use_container_width=True
)
        with tab2:
                # ==========================================
                # VISUALIZATIONS
                # ==========================================

                st.subheader("📊 Visualizations")

                numeric_cols = df.select_dtypes(
                    include=["int64", "float64"]
                ).columns.tolist()

                categorical_cols = df.select_dtypes(
                    include=["object"]
                ).columns.tolist()

                chart_type = st.selectbox(
                    "Select Chart Type",
                    [
                        "Histogram",
                        "Bar Chart",
                        "Scatter Plot",
                        "Box Plot",
                        "Pie Chart",
                        "Heatmap"
                    ]
                )

                # ==========================================
                # HISTOGRAM
                # ==========================================

                if chart_type == "Histogram":

                    column = st.selectbox(
                        "Select Numeric Column",
                        numeric_cols
                    )

                    fig = create_histogram(
                        df,
                        column
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

                # ==========================================
                # BAR CHART
                # ==========================================

                elif chart_type == "Bar Chart":

                    x_col = st.selectbox(
                        "Select X Axis",
                        df.columns
                    )

                    y_col = st.selectbox(
                        "Select Y Axis",
                        numeric_cols
                    )

                    fig = create_bar_chart(
                        df,
                        x_col,
                        y_col
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

                # ==========================================
                # SCATTER PLOT
                # ==========================================

                elif chart_type == "Scatter Plot":

                    x_col = st.selectbox(
                        "Select X Axis",
                        numeric_cols
                    )

                    y_col = st.selectbox(
                        "Select Y Axis",
                        numeric_cols,
                        index=1 if len(numeric_cols) > 1 else 0
                    )

                    fig = create_scatter_plot(
                        df,
                        x_col,
                        y_col
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

                # ==========================================
                # BOX PLOT
                # ==========================================

                elif chart_type == "Box Plot":

                    column = st.selectbox(
                        "Select Column",
                        numeric_cols
                    )

                    fig = create_box_plot(
                        df,
                        column
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

                # ==========================================
                # PIE CHART
                # ==========================================

                elif chart_type == "Pie Chart":

                    if len(categorical_cols) > 0:

                        column = st.selectbox(
                            "Select Category Column",
                            categorical_cols
                        )

                        fig = create_pie_chart(
                            df,
                            column
                        )

                        st.plotly_chart(
                            fig,
                            use_container_width=True
                        )

                    else:

                        st.warning(
                            "No categorical columns available."
                        )

                # ==========================================
                # HEATMAP
                # ==========================================

                elif chart_type == "Heatmap":

                    fig = create_heatmap(df)

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

        with tab3:
            # ==========================================
                # PDF REPORT
                # ==========================================

                st.divider()

                st.subheader("📄 Generate PDF Report")

                if st.button("Create PDF Report"):

                    with st.spinner("Generating PDF..."):

                        pdf_path = generate_pdf_report(df)

                        with open(pdf_path, "rb") as file:

                            st.download_button(
                                label="⬇ Download PDF Report",
                                data=file,
                                file_name="AI_Data_Report.pdf",
                                mime="application/pdf"
                            )
                            
                # ==========================================
                # AI INSIGHTS
                # ==========================================

                st.divider()

                st.subheader("🧠 AI Insights Generator")

                if st.button("Generate Insights"):

                    with st.spinner("Generating Insights..."):

                        insights = generate_insights(df)

                        st.success(
                            "Insights Generated Successfully"
                        )

                        st.markdown(insights)
        with tab4:
                # ==========================================
                # SQL QUERY GENERATOR
                # ==========================================

                st.divider()

                st.subheader("🗄️ AI SQL Query Generator")

                sql_question = st.text_input(
                    "Describe the SQL query you want"
                )

                if st.button("Generate SQL"):

                    if sql_question:

                        with st.spinner("Generating SQL Query..."):

                            sql_query = generate_sql_query(
                                df,
                                sql_question
                            )

                            st.success(
                                "SQL Query Generated"
                            )

                            st.code(
                                sql_query,
                                language="sql"

                            )
                            st.download_button(
                            label="⬇ Download SQL",
                            data=sql_query,
                            file_name="generated_query.sql",
                            mime="text/plain"
                        )
        with tab5:
                # ==========================================
                # AI DATASET CHATBOT
                # ==========================================

                if "chat_history" not in st.session_state:
                    st.session_state.chat_history = []

                st.divider()

                st.subheader("🤖 Ask AI About Your Dataset")

                question = st.text_input(
                    "Ask a question about your dataset"
                )

                if st.button("Ask AI"):

                    if question.strip():

                        llm = get_llm()

                        context = df.head(20).to_string()  

                        prompt = f"""
                    You are a professional Data Analyst.

                    Dataset:
                    {context}

                    Question:
                    {question}

                    Provide a detailed and professional answer.
                    """

                        response = llm.invoke(prompt)

                        answer = response.content

                        st.session_state.chat_history.append(
                            ("🧑 User", question)
                        )

                        st.session_state.chat_history.append(
                            ("🤖 AI", answer)
                        )

                        st.success("AI Response")

                        st.write(answer)

                # ==========================================
                # CLEAR CHAT
                # ==========================================

                st.divider()

                if st.button("🗑 Clear Chat"):

                    st.session_state.chat_history.clear()

                    st.rerun()

                # ==========================================
                # CHAT HISTORY
                # ==========================================

                st.subheader("💬 Chat History")

                for role, message in st.session_state.chat_history:

                    st.markdown(
                        f"**{role}:** {message}"
                    )

    except Exception as e:

        st.error(
            f"❌ Error: {str(e)}"
        )