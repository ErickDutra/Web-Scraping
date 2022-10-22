from urllib import response
import requests
from bs4 import BeautifulSoup

lista_noticias = []

def scraping():
    response = requests.get('https://g1.globo.com/')
    content = response.content
    site = BeautifulSoup(content, 'html.parser')
    noticia = site.findAll('div', attrs={'class': 'feed-post-body'})
    for noticia in noticia:
        
        titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

        subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
        
        if(subtitulo):
            lista_noticias.append([titulo.text,subtitulo.text, titulo['href']])
        else:
            lista_noticias.append([titulo.text,'', titulo['href']])
            
def salvar_txt():
    with open('noticias.txt', 'w', encoding='utf-8') as arquivo:
        for valor in lista_noticias:
            arquivo.write(str(valor)+'\n' + '\n' + '\n')



while True:
    atualizar = int(input("Desea atualizar as noticias? [1]Atualizar [0]Sair :"))
    if atualizar == 1:
        scraping()
        salvar_txt()
        print("Salvo com sucesso !!!")  
    elif atualizar == 0:
        break

print("Noticias Atualizada !!!")
