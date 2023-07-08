
# from bs4 import BeautifulSoup
# import lxml
# import requests

# response = requests.get("https://news.ycombinator.com")

# yc_webpage = response.text

# # with open("website.html", encoding='utf-8') as file:
# #     contents = file.read()

# soup = BeautifulSoup(yc_webpage, 'lxml')

# articles = soup.findAll(name="tr", class_="athing")


# article_texts = []
# article_links = []

# for article in articles:
#     title = article.find(name="span", class_="titleline")
#     title_updated = title.find(name="a")
#     title_text = title_updated.getText()
#     title_link = title_updated.get("href")
#     article_texts.append(title_text)
#     article_links.append(title_link)

# # print(article_links)
# # print(article_texts)

# article_upvotes = [int(score.getText().split()[0])
#                    for score in soup.findAll(name="span", class_="score")]


# # print(int(article_upvotes[0].split()[0]))

# # print(soup.prettify())

# # all_anchor_tags = soup.find_all(name="a")

# # print(all_anchor_tags)

# # for tag in all_anchor_tags:
# #     print(tag.get("href"))

# max_score=article_upvotes.index(max(article_upvotes))


import requests

from bs4 import BeautifulSoup

# response = requests.get(
#     "https://www.empireonline.com/movies/features/best-movies-2/")
response = requests.get(
    "https://www.cinemarealm.com/best-of-cinema/empires-500-greatest-movies-of-all-time/")

website_html_1 = response.text

soup = BeautifulSoup(website_html_1, "html.parser")

all_movies = soup.findAll(name="div", class_="entry-content")

movie_titles = [movie.getText() for movie in all_movies]

movies = movie_titles[0].split('\n')
movies.pop(0)
movies.pop(0)
movies = movies[:103]
print(movies)

with open("movies.txt", mode="w") as file:
    i = 1
    for movie in movies:
        movie = movie.split('(')
        movie = movie[0]
        file.write(f"{movie}\n")
        i += 1
