import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309'
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('.list-wrap>tbody>tr')
rank = 0
# 반복으로 돌려주기
for music in musics:
    print('-' * 60)
    #print(music)
    music_name = music.select('.info>a')
    #singer = music.select('.info>a')
    #print(singer)
    #print(name)
    if len(music_name)>0:
        rank += 1
        name = music_name[0].text.strip()
        singer = music_name[1].text
        album = music_name[2].text
    #print(rank,'-', name,'-', singer)
    jini_music = '[{}] - {} - {} /// {}'.format(rank, name, singer, album)
    print(jini_music)