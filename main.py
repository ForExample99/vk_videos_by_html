from bs4 import BeautifulSoup
import requests
url = input ('Enter a link like "https://vk.com/video/@username" please: ') #вводим ссылку на страницу с видосами из VK
#url = 'https://vk.com/video/@vestnik_tss'
headers = {
    'Accept': '*/*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.714 Yowser/2.5 Safari/537.36'
}
req = requests.get(url, headers=headers) #обращаемся к странице, забираем весь html код. headers дает понять, что мы реальный человек
src = req.text #создаем переменную с кодом страницы, просто for fun
with open('vk_videos_page.html','w') as file0: #записываем страницу в файл
    file0.write(src)
try: #пытаемся читать страницу без декодинка и с ним
    file = (open('vk_videos_page.html')).read()
except UnicodeDecodeError:
    file = (open('vk_videos_page.html', encoding='utf-8')).read()
soup = BeautifulSoup(file, 'lxml') #создаем объект супа, чтобы он разобрался как страница вообще устроена
links = soup.find_all('a', class_="VideoCard__thumbLink video_item__thumb_link") #находим все теги, в которых есть ссылка на видосы
with open('Links.html', 'w', encoding='utf-8') as file1: #открываем файл на запись и через цикл извлекаем из каждого тега ссылки
    count = 1
    for link in links:
        link_href = link.get('href')
        label = link.get('aria-label')
        file1.write(f'{count}. {label.strip()}:\nhttps://vk.com{link_href}\n')#записываем название и ссылки с новой строки
        count += 1