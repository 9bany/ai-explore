from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

complete = client.chat.completions.create(
    model="llama-3.2-3b-instruct",
    messages=[
        {"role": "system", "content": "Always answer in rhymes."},
        {"role": "user", "content": "What is Golang in programing ?"}
    ],
    temperature=0.7,
)

print(complete.choices[0].message.content)