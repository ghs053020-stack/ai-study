from openai import OpenAI

openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
messages = []

while True:
    user = input("나: ")
    if user == "exit":
        break
    messages.append({"role": "user", "content": user})
    response = openai.chat.completions.create(model="llama3.2", messages=messages)
    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})
    print("AI:", answer)
