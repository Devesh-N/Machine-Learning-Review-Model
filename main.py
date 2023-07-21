import pickle
from bs4 import BeautifulSoup
from nltk.stem.porter import PorterStemmer
import re

# Load the model and vectorizer
model = pickle.load(open("movie_review_model.pkl", "rb"))
vectorizer = pickle.load(open("movie_review_vectorizer.pkl", "rb"))

# Define the list of stopwords and the stemmer
stopwords = [...]  # Use the list of stopwords we defined earlier
stemmer = PorterStemmer()

# Function to preprocess text
def preprocess_text(text):
    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()

    # Remove special characters/numbers
    text = re.sub('[^a-zA-Z]', ' ', text)

    # Convert to lower case and split into words
    words = text.lower().split()

    # Remove stopwords and stem the words
    words = [stemmer.stem(word) for word in words if word not in stopwords]

    # Join the words back into a string
    text = ' '.join(words)

    return text

# Function to predict the sentiment of a review
def predict_sentiment(review):
    # Preprocess the review
    review = preprocess_text(review)

    # Vectorize the review
    review_vector = vectorizer.transform([review])

    # Predict the sentiment of the review
    sentiment = model.predict(review_vector)

    return "positive" if sentiment[0] == 1 else "negative"

# Example usage:
review = "it's a inspiring movie"
print(predict_sentiment(review))  # Output: "positive"
