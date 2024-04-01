import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
ps=PorterStemmer()

tfidf=pickle.load(open('vectori.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title("Email:Spam Classifier")

input_sms=st.text_area("Enter Message")



def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return ' '.join(y)

if st.button("Predict"):
    #preprocessing
    transformed_sms=transform_text(input_sms)
    #vectorizing
    vector_input=tfidf.transform([transformed_sms])
    #prediction
    result=model.predict(vector_input)[0]
    #display
    if result==1:
        st.header("Spam")
    else:
        st.header('Not spam')