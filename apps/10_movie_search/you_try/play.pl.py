import requests
import collections

# omdb api url http://www.omdbapi.com/?i=tt3896198&apikey=a2f13739
# omdb api key a2f13739

search = 'capital'
url = 'http://www.omdbapi.com?s={}&apikey=a2f13739'.format(search)

r = requests.get(url)
data = r.json()

results = data['Search']

movies = []
    for result in results:
        m = MovieResult()
