# 🤖 AI Data Analyst

An AI-powered data analysis application that allows users to upload datasets, explore and analyze data, generate visualizations, ask questions in natural language, and create AI-powered insights and reports.

The application combines **Python, Pandas, Streamlit, SQL, LLMs, and data visualization** to provide an interactive data analysis experience without requiring users to write complex code manually.

---

## 🚀 Project Overview

**AI Data Analyst** is designed to automate common data analysis tasks.

Users can upload a CSV dataset and use the application to:

* 📂 Upload and analyze datasets
* 🔍 Explore dataset structure and statistics
* 📊 Generate different visualizations
* 🤖 Ask questions about the dataset using natural language
* 🧠 Generate AI-powered insights
* 🗃️ Generate SQL queries using an LLM
* 📄 Generate automated analysis reports
* 📑 Export analysis results as a PDF report

---

## ✨ Features

### 1. 📂 Data Upload

Users can upload their own CSV dataset through the Streamlit interface.

The application automatically loads the dataset and prepares it for analysis.

### 2. 🔎 Dataset Analysis

The application provides information such as:

* Number of rows and columns
* Column names
* Data types
* Missing values
* Statistical summary
* Unique values
* Numerical and categorical columns

### 3. 📊 Data Visualization

Users can generate multiple types of visualizations, including:

* Histogram
* Bar Chart
* Scatter Plot
* Box Plot
* Pie Chart
* Correlation Heatmap

These visualizations help users understand patterns, relationships, distributions, and outliers in their datasets.

### 4. 🤖 AI-Powered Insights

An LLM is integrated into the application to analyze the dataset and generate meaningful insights.

The AI can identify:

* Important patterns
* Trends
* Relationships between variables
* Potential anomalies
* Business insights
* Recommendations

### 5. 🗃️ Natural Language to SQL

Users can ask questions about their data using natural language.

For example:

> "What is the average sales by region?"

The application can generate an appropriate SQL query using the LLM.

### 6. 📄 Automated Report Generation

The application can generate an analysis report containing:

* Dataset summary
* Statistical information
* Visualizations
* AI-generated insights
* Analysis results

The report can be exported as a PDF.

---

## 🛠️ Technologies Used

| Technology   | Purpose                          |
| ------------ | -------------------------------- |
| Python       | Core programming language        |
| Pandas       | Data loading and analysis        |
| NumPy        | Numerical operations             |
| Streamlit    | Web application interface        |
| Matplotlib   | Data visualization               |
| Seaborn      | Statistical visualization        |
| SQL          | Data querying                    |
| LangChain    | LLM integration                  |
| LLM API      | AI-powered analysis and insights |
| ReportLab    | PDF report generation            |
| Git & GitHub | Version control                  |

---

## 🏗️ Project Architecture

```text
AI_DATA_ANALYST/
│
├── data/
│   └── Dataset files
│
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── data_loader.py
│   ├── insights.py
│   ├── llm.py
│   ├── report_generator.py
│   ├── sql_generator.py
│   └── visualizer.py
│
├── uploads/
│   └── Uploaded datasets
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🔄 Application Workflow

```text
User Uploads Dataset
        ↓
   Data Loader
        ↓
 Data Preprocessing
        ↓
 ┌───────────────┐
 │ Data Analysis │
 └───────────────┘
        ↓
 ┌───────────────┬────────────────┐
 ↓               ↓                ↓
Statistics   Visualization   SQL Generation
 ↓               ↓                ↓
 └───────────────┴────────────────┘
                 ↓
           LLM Integration
                 ↓
        AI-Generated Insights
                 ↓
          Report Generation
                 ↓
              PDF Report
```

---

## 📁 Module Description

### `app.py`

Main Streamlit application.

Responsible for:

* User interface
* Dataset upload
* Calling analysis functions
* Displaying visualizations
* Displaying AI insights
* Generating reports

### `data_loader.py`

Handles dataset loading and preparation.

### `analyzer.py`

Performs data analysis operations such as:

* Dataset summary
* Statistical analysis
* Data type analysis
* Missing-value analysis

### `visualizer.py`

Creates different charts and visualizations from the dataset.

### `llm.py`

Handles the connection between the application and the selected Large Language Model.

### `insights.py`

Uses the LLM to generate meaningful insights from the dataset.

### `sql_generator.py`

Converts natural-language questions into SQL queries.

### `report_generator.py`

Generates automated PDF reports containing the analysis results and insights.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI_DATA_ANALYST.git
```

### 2. Navigate to the Project

```bash
cd AI_DATA_ANALYST
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root directory.

Add your LLM API key:

```env
GROQ_API_KEY=your_api_key_here
```

> Never upload your `.env` file or API keys to GitHub.

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 Example Questions

Users can ask questions such as:

```text
What are the main trends in this dataset?
```

```text
Which category has the highest sales?
```

```text
What is the average value of the numerical columns?
```

```text
Are there any unusual values or outliers?
```

```text
Generate insights from this dataset.
```

```text
Show me the relationship between sales and profit.
```

---

## 📊 Key Capabilities

| Capability               | Available |
| ------------------------ | --------- |
| CSV Upload               | ✅         |
| Dataset Summary          | ✅         |
| Statistical Analysis     | ✅         |
| Missing Value Analysis   | ✅         |
| Data Visualization       | ✅         |
| AI Insights              | ✅         |
| Natural Language Queries | ✅         |
| SQL Query Generation     | ✅         |
| PDF Report Generation    | ✅         |
| Streamlit Interface      | ✅         |

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Automate repetitive data analysis tasks.
2. Make data analysis accessible to non-technical users.
3. Allow users to interact with datasets using natural language.
4. Generate meaningful insights using LLMs.
5. Combine traditional data analysis with Generative AI.
6. Automatically generate professional analysis reports.

---

## 🔮 Future Improvements

Potential future enhancements include:

* Support for Excel files
* Support for multiple datasets
* Conversational memory
* Advanced data cleaning
* Automatic feature engineering
* More advanced SQL execution
* Interactive dashboards
* Streaming AI responses
* Cloud deployment
* Authentication and user management

---

## 👨‍💻 Author

**Abisheik**

B.Tech – Information Technology

### Skills Demonstrated

* Python
* Data Analysis
* SQL
* Machine Learning
* Generative AI
* LLM Integration
* LangChain
* Data Visualization
* Streamlit
* API Integration
* PDF Report Generation
---