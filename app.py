import streamlit as st
from PIL import Image

email_contact = "tucorreo@hotmail.com"
st.set_page_config(page_title="SGP ",page_icon="🔖", layout="wide")

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

css_load("style/main.css")

#intro
with st.container():
    st.title("SISTEMA DE GESTIÓN DE PRECIOS")
    st.header("Hola, este es el sistema de gestión de precios de Ecommerce 👋")
    st.write("Este es el sistema con el cual los Category Manager definen los precios de los producots que Ecommerce venderá.")
    st.write("[Saber más >](https://tiendanewsan.com.ar/)")

# sobre nosotros
with st.container():
    st.write("---")
    text_column, animation_column = st.columns(2)
    with text_column:
        st.header("Sobre nosotros 💯")
        st.write(
            """
            Nuestro objetivo es poder aportar valor a los negocios de Ecommerce a ahorrar tiempo y dinero.
            Seguramente vamos a poder ayudar si:

            - Tenes un producto sin precio
            - Sos parte del equipo de Categories
            - Tenes ganas de trabajar

            ***Si esto suena interesante para vos podes contactarnos a través del formulario***
            """
        )
        st.write("[Más sobre nosotros >](https://tiendanewsan.com.ar/about/)")
    with animation_column:
        st.empty()

# Servicios
with st.container():
    st.write("---")
    st.header("Servicios")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("imagenes/apps.jpg")
        st.image(image,use_column_width=True)
    with text_column:
        st.subheader("Diseño e aplicaciones")
        st.write(
            """
            Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación
            """
        )
        st.write("[Ver servicios >](https://tiendanewsan.com.ar/)")
    
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("imagenes/apps.jpg")
        st.image(image,use_column_width=True)
    with text_column:
        st.subheader("Diseño e aplicaciones")
        st.write(
            """
            Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación
            """
        )
        st.write("[Ver servicios >](https://tiendanewsan.com.ar/)")

    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("imagenes/apps.jpg")
        st.image(image,use_column_width=True)
    with text_column:
        st.subheader("Diseño e aplicaciones")
        st.write(
            """
            Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación
            """
        )
        st.write("[Ver servicios >](https://tiendanewsan.com.ar/)")

# contacto
with st.container():
    st.write("---")
    st.header("Contactanos:")
    st.write("##")
    contact_form = """
    <form action="htttps://formsubmit.co/{email_contact}" method="POST">
      <input type="hidden" name="_captcha" value="false">
      <input type="text" name="name" placeholder="Tu nombre" required>
      <input type="email" name="email" placeholder="Tu email" required>
      <textarea type="message" name="message" placeholder="Tu mensaje aquí" required></textarea>
      <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()