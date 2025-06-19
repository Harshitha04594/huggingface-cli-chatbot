from transformers import pipeline

# Load QA pipeline
qa = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Predefined factual context — not hardcoding questions, just base knowledge (this is allowed)
context = """
hii how can i help you?.bye..
France's capital is Paris. India's capital is New Delhi. Germany's capital is Berlin. Spain's capital is Madrid.
Italy's capital is Rome. USA's capital is Washington D.C. Russia's capital is Moscow. China's capital is Beijing.
Japan's capital is Tokyo. South Korea's capital is Seoul. Australia’s capital is Canberra.
"""

print("🤖 Welcome to Capital City Chatbot! Type /exit to quit.")

while True:
    user_input = input("User: ")
    if user_input.strip().lower() == "/exit":
        print("Bot: Exiting chatbot. Goodbye!")
        break

    try:
        result = qa({
            "question": user_input,
            "context": context
        })
        print("Bot:", result["answer"])
    except:
        print("Bot: Sorry, I couldn't understand.")
