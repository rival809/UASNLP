import pandas as pd
import re
import string

from io import StringIO
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

data1 = pd.read_csv('data\Data Scraper - Indodax.csv')
data = pd.concat([data1])


def cleaning(text):
    return text


data['Content'] = data['Content'].apply(lambda x: cleaning(x))
data['Content'].values

# Create Sastrawi stemmer
stemmer = StemmerFactory().create_stemmer()

# Create Stopword
with open("data\stopwords-id.txt", "r") as f:
    stop_words = f.readline()
    stop_words = stop_words.split()

    # Preprocessor


def preprocessor(text):
    # Convert to lower case
    text = text.lower()
    # Remove additional code
    text = text.replace('\\xe2\\x80\\xa6', '')
    # Convert www.* or https?://* to URL
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', text)
    # Convert @username to AT_USER
    text = re.sub('@[^\s]+', '', text)
    # Remove additional white spaces
    text = re.sub('[\s]+', ' ', text)
    # Replace #word with word
    text = re.sub(r'#([^\s]+)', r'\1', text)
    # Menghapus angka dari teks
    text = re.sub(r"\d+", "", text)
    # Menganti tanda baca dengan spasi
    text = text.translate(str.maketrans(
        string.punctuation, ' ' * len(StringIO.punctuation)))
    return text


data['Content'] = data['Content'].apply(lambda x: preprocessor(x))
data['Content'].values

# Fungsi save hasil data yang sudah dibersihkan
# data.to_csv('../output/cleaned_data.csv')
