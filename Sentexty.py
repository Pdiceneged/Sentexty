from nltk.sentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
import nltk
import streamlit as st
import base64

st.set_page_config(
        page_title="Análise de Sentimento",
        page_icon="👍"
    )

@st.cache_data()
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("fundo4k.png")
img2 = get_img_as_base64("pdifundo2.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:fundo4k/png;base64,{img}");
    background-size: 100%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
[data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:pdifundo2/png;base64,{img2}");
    background-position: center; 
    background-size: 100%;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
    right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.image("Logopdi.png", width=280)


def translate_text(text):
    translator = GoogleTranslator(source='pt', target='en')
    translated_text = translator.translate(text)
    return translated_text

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    return sentiment_score

def main():

    st.title("Análise de Sentimento")
    nltk.download('vader_lexicon')
    text = st.text_area("Digite o texto a ser analisado:", "")

    if st.button("Analisar", key="analyze_button", help="Clique para analisar o sentimento"):
        if text:
            translated_text = translate_text(text)
            sentiment_result = analyze_sentiment(translated_text)
            sentiment_percentage = (sentiment_result['compound'] + 1) * 50

            if sentiment_result['compound'] >= 0.05:
                result = "Positivo"
                color = "green"
            elif sentiment_result['compound'] <= -0.05:
                result = "Negativo"
                color = "red"
            else:
                result = "Neutro"
                color = "yellow"

            st.markdown(f"**Sentimento:** <span style='color:{color}'>{result}</span>", unsafe_allow_html=True)

            st.markdown(f"**Positividade do sentimento em porcentagem:** {sentiment_percentage:.2f}%", unsafe_allow_html=True)

            with st.expander("Detalhes da Pontuação de Sentimento"):
                st.markdown(f"**Negativo:** <span style='color:red'>{sentiment_result['neg'] * 100:.2f}%</span>", unsafe_allow_html=True)
                st.markdown(f"**Neutro:** <span style='color:yellow'>{sentiment_result['neu'] * 100:.2f}%</span>", unsafe_allow_html=True)
                st.markdown(f"**Positivo:** <span style='color:green'>{sentiment_result['pos'] * 100:.2f}%</span>", unsafe_allow_html=True)
                st.markdown(f"**Compound:** {sentiment_result['compound']:.4f}")
        else:
            st.warning("Digite um texto para análise.")

if __name__ == "__main__":
    main()

st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por [PedroFS](https://linktr.ee/Pedrofsf)")
