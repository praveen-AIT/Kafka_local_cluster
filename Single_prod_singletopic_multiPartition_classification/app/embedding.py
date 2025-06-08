from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Dummy dataset for fitting TF-IDF
corpus = [
    "buy now limited offer",  # spam
    "this is a normal user review",  # ham
    "win cash prize click here",  # spam
    "thank you for your feedback",  # ham
]

# Fit TF-IDF once (you can load/save model in prod)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
spam_labels = np.array(["SPAM", "HAM", "SPAM", "HAM"])

def classify_text(text: str) -> str:
    vec = vectorizer.transform([text])
    # cosine similarity with all vectors
    similarities = vec @ X.T  # shape (1, len(corpus))
    most_similar_idx = similarities.argmax()
    return spam_labels[most_similar_idx]
