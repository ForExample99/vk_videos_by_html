from bs4 import BeautifulSoup
try:
    file = (open('vk_videos_page.html')).read()
except UnicodeDecodeError:
    file = (open('vk_videos_page.html', encoding='utf-8')).read()
#print(file)
soup = BeautifulSoup(file, 'lxml')
links = soup.find_all('a', class_="VideoCard__thumbLink video_item__thumb_link")
with open('Links.html', 'w', encoding='utf-8') as file1:
    for link in links:
        link_href = link.get('href')
        label = link.get('aria-label')
        file1.write(f'{label.strip()}:\nhttps://vk.com{link_href}\n')