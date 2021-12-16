import json
import pandas as pd
from tqdm import tqdm

import seaborn as sns
import matplotlib.pyplot as plt

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

from google_play_scraper import Sort, reviews, app


sns.set(style='whitegrid', palette='muted', font_scale=1.2)

##Aplikasi yang akan dilakukan data scraping, ditulis nama packagenya. Dapat ditambahkan lebih dari 1 aplikasi
##Disini kami mengambil review dari aplikasi indodax di playstore
app_packages = [
  'id.co.bitcoin',
]

##Scraping informasi aplikasi
app_infos = []

for ap in tqdm(app_packages):
  info = app(ap, lang='id', country='id')
  del info['comments']
  app_infos.append(info)

##Merubah data hasil scraping ke dalam bentuk JSON
def print_json(json_object):
  json_str = json.dumps(
    json_object, 
    indent=2, 
    sort_keys=True, 
    default=str
  )
  print(highlight(json_str, JsonLexer(), TerminalFormatter()))

##Data JSON dari aplikasi yang telah dilakukan scraping
##print_json(app_infos[0])

##This contains lots of information including the number of ratings, number of reviews and number of ratings for each score (1 to 5). Let's ignore all of that and have a look at their beautiful icons:
  def format_title(title):
    sep_index = title.find(':') if title.find(':') != -1 else title.find('-')
    if sep_index != -1:
      title = title[:sep_index]
    return title[:10]
  
  fig, axs = plt.subplots(2, len(app_infos) // 2, figsize=(14, 5))
  for i, ax in enumerate(axs.flat):
      ai = app_infos[i]
      img = plt.imread(ai['icon'])
      ax.imshow(img)
      ax.set_title(format_title(ai['title']))
      ax.axis('off')

##Konversi JSON objects menjadi Pandas dataframe dan menyimpan hasil menjadi CSV file:
app_infos_df = pd.DataFrame(app_infos)
app_infos_df.to_csv('apps.csv', index=None, header=True)

##Scraping App Reviews
app_reviews = []

for ap in tqdm(app_packages):
  for score in list(range(1, 6)):
    for sort_order in [Sort.MOST_RELEVANT, Sort.NEWEST]:
      rvs, _ = reviews(
        ap,
        lang='id',
        country='id',
        sort=sort_order,
        count= 200 if score == 3 else 100,
        filter_score_with=score
      )
      for r in rvs:
        r['sortOrder'] = 'most_relevant' if sort_order == Sort.MOST_RELEVANT else 'newest'
        r['appId'] = ap
      app_reviews.extend(rvs)

##print_json(app_reviews[0])

##Export data ke csv
app_reviews_df = pd.DataFrame(app_reviews)
app_reviews_df.to_csv(f'output\Hasil Scraping.csv', index=None, header=True)