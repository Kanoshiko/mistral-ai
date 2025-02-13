from mistralai import Mistral
import streamlit as st

client = Mistral(api_key="1lFl56MeZF5OE8jCiGeIYAz28qzcrmM2")

# Titre
st.title("Analyse une image avec Mistral AI")

prompt = st.text_input("Entrez l'url de l'image")

# Analyse d'image unique
if st.button("Envoyer") :
  chat_response = client.chat.complete(
      model = "pixtral-12b-2409",
      messages= [
      {
          "role": "user",
          "content": [
              {
                  "type": "text",
                  "text": "Que contient cette image ?"
              },
              {
                  "type": "image_url",
                  "image_url": prompt
              }
          ]
      }
  ]
  )

  st.write(chat_response.choices[0].message.content)
