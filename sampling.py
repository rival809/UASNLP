import numpy as np
import pandas as pd
import os

from datetime import datetime

##Load data ke memmory menggunakan library pandas. 
data = pd.read_csv('data\Data Scraper - Indodax.csv')

##Menghapus data yang berduplikasi
data1 = data.drop_duplicates('Content')

##Dilakukan sampling menggunakan method `sample` dari library `pandas` sebanyak 700 data.
##Note : Naikan banyak sample agar model yang dibuat lebih baik dan relevant terhadap banyak kasus
BANYAK_SAMPLE_DATA = 700
sample = data1.sample(n=BANYAK_SAMPLE_DATA, random_state=2020)
    
##Export sample dataset
sample.to_csv (f'output\{datetime.today().strftime("%Y-%m-%d")} - Sample_review.csv')



