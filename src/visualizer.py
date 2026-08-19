import plotly.express as px


def create_histogram(df, column):
    fig = px.histogram(
        df,
        x=column,
        nbins=20,
        marginal="box",
        title=f"Distribution of {column}",
        template="plotly_dark"
    )
    return fig


def create_bar_chart(df, x_col, y_col):
    fig = px.bar(
        df,
        x=x_col,
        y=y_col,
        title=f"{y_col} by {x_col}",
        template="plotly_dark"
    )
    return fig


def create_scatter_plot(df, x_col, y_col):
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        title=f"{x_col} vs {y_col}",
        template="plotly_dark"
    )
    return fig


def create_box_plot(df, column):
    fig = px.box(
        df,
        y=column,
        title=f"Box Plot of {column}",
        template="plotly_dark"
    )
    return fig


def create_pie_chart(df, column):
    counts = df[column].value_counts().reset_index()
    counts.columns = [column, "Count"]

    fig = px.pie(
        counts,
        names=column,
        values="Count",
        title=f"Distribution of {column}",
        template="plotly_dark"
    )
    return fig


def create_heatmap(df):
    corr = df.select_dtypes(
        include=["int64", "float64"]
    ).corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Heatmap"
    )

    return fig