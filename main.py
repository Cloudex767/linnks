#My linktr.ee
import streamlit as st 
from PIL import Image

st.set_page_config( page_icon="✈️", page_title="Rian Vinícius")

def main():
    col1, col2, col3 = st.columns([1,1,1])
    image = Image.open("foto.png")
    img = image.resize((280,280))
    with col2:
        st.image(img)
        st.title("RIAN VINÍCIUS")
    st.write("---")
    with st.expander("🖥 Desenvolvimento de software"):
        st.button("Mega pack de ferramentas - Em breve", use_container_width=True)
        st.write("---")
        st.write("Habilidades: \n"
                 "- Python;\n"
                 "- Web (HTML, CSS e JS)\n"
                 "- Desenvolvimento android;\n")
        st.link_button("Contato para serviços ...","https://api.whatsapp.com/send?phone=5532991458306&text=Ol%C3%A1,%20tenho%20interesse%20nos%20servi%C3%A7os%20de%20programação",use_container_width=True)       
    with st.expander("✨ Designer"):
        st.button("Acesse meu portifolio: - Em breve", use_container_width=True)
        st.write("---")
        st.write("- 172h de: Coreldraw X6 , Photoshop CS6 , \n"
                 "Flash CS6 , Autocad , 3D Studio")
        st.link_button("Contato para serviços ...","https://api.whatsapp.com/send?phone=5532991458306&text=Ol%C3%A1,%20tenho%20interesse%20nos%20servi%C3%A7os%20de%20designer", use_container_width=True)
    with st.expander("🗞 Artes"):
        st.write("Sou artista especializado em desenho realista. Minha paixão é capturar a beleza e a complexidade do mundo com detalhes precisos e mensagens empolgantes. Através de cada linha e sombra, busco refletir a verdadeira essência dos meus sujeitos, seja em retratos, paisagens ou objetos cotidianos. Estou aberto a novos desafios e colaborações. Se desejar saber mais sobre meu trabalho, estou à disposição.")
        st.write("---")
        st.button("Veja minhas artes - Em breve", use_container_width=True)
        st.link_button("Instagram","https://www.instagram.com/rianvinicius_/", use_container_width=True)
    st.link_button("Instagram dedicado a aviação", "https://www.instagram.com/art_aviation14/", use_container_width=True)
    st.write("---")
    st.write("Acesse meu currículum")
    #file_path = 'curriculo-rian.pdf'
    #with open(file_path, 'rb') as file:
        #file_data = file.read()
    #st.download_button(label="Baixar PDF",data=file_data,file_name='curriculo-rian.pdf',mime='./', use_container_width=True)
    st.link_button("Contato direto","https://api.whatsapp.com/send?phone=5532991458306", use_container_width=True)
    st.write("")
    col4, col5, col6 = st.columns([1,1,1])
    with col5:
        st.write("A app by: Rian Vinícius | Todos os direitos reservados © 2024", use_container_width=True)
    
main()

        
    
