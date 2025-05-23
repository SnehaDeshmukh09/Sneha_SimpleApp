import os
import streamlit as st
from openai import OpenAI

# Load API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="Omelette Recipes Chatbot", page_icon="🍳")
st.title("🌍 Omelette Recipe Chatbot")

st.markdown("Ask me how to make an omelette from different parts of the world!")

# Chat input
user_input = st.text_input("You:", placeholder="How do I make a Japanese omelette?")

if user_input:
    with st.spinner("Cooking up your recipe..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4",  # or "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": "You are a culinary expert who specializes in international omelette recipes."},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                max_tokens=500
            )

            recipe = response.choices[0].message.content
            st.markdown("### 🍽️ Here's your recipe:")
            st.markdown(recipe)

        except Exception as e:
            st.error(f"Error: {e}")
