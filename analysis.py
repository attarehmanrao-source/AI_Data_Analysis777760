import pandas as pd
from groq import Groq

# 1. ڈیش بورڈ کے لیے سمری کا فنکشن
def get_summary(df):
    summary = {
        "Total Rows": int(df.shape[0]),
        "Total Columns": int(df.shape[1]),
        "Columns": list(df.columns),
        "Missing Values": int(df.isnull().sum().sum())
    }
    return summary

# 2. Groq AI سے جواب حاصل کرنے کا فنکشن (اپ ڈیٹ شدہ ماڈل کے ساتھ)
def get_groq_response(client, data_summary, question):
    try:
        completion = client.chat.completions.create(
            # یہاں نیا ماڈل نام استعمال کیا گیا ہے
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful data analyst. Here is the data summary: {data_summary}"
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=0.5,
            max_tokens=1024,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"ایرر: {str(e)}"