import gradio as gr
from transformers import pipeline

# Pipeline garanti disponible : analyse de sentiment
analyseur_sentiment = pipeline("sentiment-analysis")

# Fonction qui analyse le texte
def analyser_texte(texte_utilisateur):
    if len(texte_utilisateur.strip()) == 0:
        return "Écris quelque chose d'abord !"
    resultat = analyseur_sentiment(texte_utilisateur)
    return f"Label : {resultat[0]['label']}, Score : {resultat[0]['score']:.2f}"

# Interface Gradio
interface = gr.Interface(
    fn=analyser_texte,
    inputs=gr.Textbox(lines=3, placeholder="Écris ton texte ici..."),
    outputs="text",
    title="Analyseur de sentiment IA",
    description="Écris un texte et l'IA va te dire si le sentiment est positif ou négatif."
)

interface.launch(server_name="0.0.0.0", server_port=7860) 