from src.llm import get_llm


def generate_sql_query(df, user_question):

    llm = get_llm()

    columns = ", ".join(df.columns)

    prompt = f"""
You are an expert SQL developer.

Dataset Columns:
{columns}

User Request:
{user_question}

Generate only SQL query.

Do not provide explanation.
Return only SQL code.
"""

    response = llm.invoke(prompt)

    return response.content