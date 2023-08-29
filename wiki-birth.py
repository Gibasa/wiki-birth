import pandas as pd
import wikipedia as wp

print("Vamos descobrir um artigo publicado no Brasil no site Wikipedia na data de seu nascimento?")
user_birth = input("Insira a data com o formato de dd/mm/aaaa: ")

wp.set_lang("pt")
data = pd.read_csv("data.csv")
ids = data["Id"].tolist()
names = data["Name"].tolist()
births = data["Birth"].tolist()
titles = []
urls = []
summarys = []

new_data = []

user_articles = wp.search(f"\"{user_birth}\"")
user_article = wp.page(user_articles[0])
user_article_url = user_article.url
user_article_title = user_article.title

if user_article:
    print(
        f"No dia que você nasceu um dos artigos publicados foi: {user_article_title}. "
        f"\n Se quiser ler por completo esse é o link: {user_article_url}. ")


def search_article(births):
    articles = wp.search(f"\"{births}\"")
    if articles:
        article = wp.page(articles[0])
        article_title = article.title
        article_url = article.url
        article_summary = article.summary
        flag = 1
    else:
        article = None
        article_title = None
        article_url = None
        article_summary = None
        flag = 0
    return article, article_title, article_url, article_summary, flag


for id in ids:
    article_info = search_article(births[id - 1])
    if article_info[4]:
        titles.append(article_info[1])
        urls.append(article_info[2])
        summarys.append(article_info[3])
    else:
        titles.append(f"Não há nenhum artigo na data de {births[id]}")
        urls.append("N/A")
        summarys.append("N/A")

for id, name, birth, title, url, summary in zip(ids, names, births, titles, urls, summarys):
    pessoa = {
        "id": id,
        "name": name,
        "birth": birth,
        "title": title,
        "url": url,
        "summary": summary
    }
    new_data.append(pessoa)

df = pd.DataFrame(new_data)
file_name = "new_data.csv"
df.to_csv(file_name, index=False)
