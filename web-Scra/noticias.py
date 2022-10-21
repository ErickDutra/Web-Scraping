from urllib import response
import requests
from bs4 import BeautifulSoup

lista_noticias = []

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# html da noticia
noticia = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticia:
    
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
    
    if(subtitulo):
        lista_noticias.append([titulo.text,subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text,'', titulo['href']])
        

with open('noticias.txt', 'w') as arquivo:
    for valor in lista_noticias:
        arquivo.write(str(valor)+'\n' + '\n' + '\n')

