from src.llm import get_llm


def generate_insights(df):

    llm = get_llm()

    data_sample = df.sample(min(len(df), 20)).to_string()
    
    prompt = f"""
    You are a Senior Data Analyst.

    Dataset:
    {data_sample}

    Generate:

    1. Key Insights
    2. Patterns
    3. Trends
    4. Anomalies
    5. Business Recommendations

    Return in bullet points.
    """

    response = llm.invoke(prompt)

    return response.content