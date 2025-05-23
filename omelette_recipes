import os
import openai
import streamlit as st

# Access OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Omelette Recipes Chatbot", page_icon="🍳")
st.title("🌍 Omelette Recipe Chatbot")

st.markdown("Ask me how to make an omelette from different parts of the world!")

# Chat interface
user_input = st.text_input("You:", placeholder="How do I make a Spanish omelette?")

if user_input:
    with st.spinner("Cooking up your recipe..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # or gpt-3.5-turbo
                messages=[
                    {"role": "system", "content": "You are a culinary expert who specializes in international omelette recipes."},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                max_tokens=500
            )

            recipe = response['choices'][0]['message']['content']
            st.markdown("### 🍽️ Here's your recipe:")
            st.markdown(recipe)

        except Exception as e:
            st.error(f"Error: {e}")
