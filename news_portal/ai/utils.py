from transformers import pipeline

# Função para gerar resumo
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Função para detectar fake news
def detect_fake_news(text):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    labels = ["fake news", "real news"]
    result = classifier(text, candidate_labels=labels)
    return result['labels'][0] == "fake news"
