from nltk.sentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
import nltk
import streamlit as st

def translate_text(text):
    translator = GoogleTranslator(source='pt', target='en')
    translated_text = translator.translate(text)
    return translated_text

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    return sentiment_score

def main():
    # Configurando o ícone e o título da aba do navegador
    st.set_page_config(
        page_title="Análise de Sentimento",
        page_icon="👍"
    )

    # Usar st.sidebar.image para adicionar a imagem ao sidebar
    st.sidebar.image("Logopdi.png", width=280)

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
