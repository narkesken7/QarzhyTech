from openai import OpenAI
import pandas as pd

# Initialize the OpenAI client with the API key
client = OpenAI(api_key="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")  # Replace with your actual API key


# Load financial data from a CSV file
def load_financial_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Financial Data Loaded Successfully.")
        print(df.head())
        return df
    except FileNotFoundError:
        print("Error: File not found. Ensure the file path is correct.")
        return None


# Function to interact with GPT and generate financial insights
def generate_insights(data):
    # Convert the DataFrame to a summary string
    data_summary = data.to_string(index=False)

    # Define a prompt for GPT
    prompt = f"""
    Analyze the following financial data and provide insights:
    {data_summary}

    1. Summarize the key financial trends over the years.
    2. Suggest strategies to improve cash flow and investments.
    3. Predict future financial outcomes based on historical data.
    4. Highlight any anomalies or interesting patterns.

    Provide your analysis in a detailed yet easy-to-understand manner.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def finance_assistant():
    csv_file = "/Users/keshubai/Downloads/apple_income_statement.csv"
    financial_data = load_financial_data(csv_file)

    if financial_data is not None:
        insights = generate_insights(financial_data)
        print("\nFinancial Insights:")
        print(insights)


# Run
if __name__ == "__main__":
    finance_assistant()
