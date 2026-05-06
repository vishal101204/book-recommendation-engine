# Import Libraries
import streamlit as st
import pickle
import pandas as pd

# Load Data 
books = pickle.load(open('books.pkl', 'rb'))
similarity = pickle.load(open('books_similarity.pkl', 'rb'))

# Recommendation Function
def recommend(book):
    book = book.lower()

    if book not in books['title'].str.lower().values:
        return ["Book not found"]

    index = books[books['title'].str.lower() == book].index[0]

    distances = list(enumerate(similarity[index]))
    books_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    recommended = []
    for i in books_list:
        recommended.append(books.iloc[i[0]].title)

    return recommended

# UI
st.title("Book Recommendation System using NLP")

# Dropdown
book_list = books['title'].values
selected_book = st.selectbox("Select a book", book_list)

# Button
if st.button("Recommend"):
    recommendations = recommend(selected_book)

    st.subheader("Top 5 Recommendations:")
    for i, book in enumerate(recommendations):
        st.write(f"{i+1}. {book}")