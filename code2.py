import streamlit as st

st.title("🧢 Bring Hats - Prueba")
st.write("¡Si ves esto, Streamlit está funcionando!")

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.success(f"¡Hola {nombre}! Bienvenido a Bring Hats 🎉")

if st.button("Presiona aquí"):
    st.balloons()
    st.write("¡Funciona perfecto! ✅")
