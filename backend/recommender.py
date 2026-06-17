import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load dataset
df = pd.read_csv("dataset/career_data.csv")


# Convert skills into vectors
vectorizer = TfidfVectorizer()

skill_matrix = vectorizer.fit_transform(
    df["Skills"]
)


def recommend_career(user_skills):

    # Convert user input into vector
    user_vector = vectorizer.transform(
        [user_skills]
    )

    # Find similarity
    similarity = cosine_similarity(
        user_vector,
        skill_matrix
    )

    # Get best matching career
    index = similarity.argmax()

    recommendation = df.iloc[index]

    return recommendation     