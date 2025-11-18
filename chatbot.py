import gradio
from groq import Groq
client = Groq(
    api_key="******",
)
def initialize_messages():
    return [{
        "role": "system",
        "content": "You are a skilled fashion designer who gives expert, creative advice on styling, "
        "colors, fabrics, trends, wardrobe planning, and outfit suggestions."
    }]
messages_prmt = initialize_messages()
print(type(messages_prmt))
def customLLMBot(user_input, history):
    global messages_prmt
    messages_prmt.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})
    return LLM_reply
iface = gradio.ChatInterface(
    customLLMBot,
    chatbot=gradio.Chatbot(height=300),
    textbox=gradio.Textbox(placeholder="Ask your fashion question"),
    title="Fashion Designer ChatBot",
    description="Your personal styling & outfit guide",
    theme="soft",
    examples=[
        "Hi",
        "Wedding outfit idea",
        "Which color suits me?",
        "Latest trends?",
        "How to style a saree?",
        "Best summer fabrics?",
        "Minimal wardrobe tips",
        "Formal outfit for interview",
        "Accessory matching tips"
    ]
)
iface.launch(share=True)























