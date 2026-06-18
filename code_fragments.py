from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans


## ------------------------------------------------------ ##
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = embedding_model.encode(texts)

kmeans = KMeans(n_clusters = 3, random_state = 42)
cluster_labels = kmeans.fit_predict(embeddings)

## ------------------------------------------------------ ##
ERROR_CATEGORIES = ["calculation_error",
                    "reasoning_error",
                    "incomplete_solution",
                    "format_error",
                    "other"]

prompt = f"""Analyze this math error and categorize it:
            PROBLEM: {question}...
            CORRECT: {correct_answer}
            PREDICTED: {predicted_answer}
            Choose ONE category: {', '.join(ERROR_CATEGORIES)}
            Respond with just the category name."""
