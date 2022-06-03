

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib



a = input('상품명:')


query= urllib.parse.quote(a)

target_site = f'https://search.shopping.naver.com/search/all?query={query}&pagingIndex=1&pagingSize=40&productSet=total'
url = target_site





res = urlopen(url)

soup = BeautifulSoup(res, 'html5lib')

for td in soup.select('.basicList_title__3P9Q7'):   
    print(td.a.string.strip()) 
f = open('파일명1.txt', 'w')

f.write('')

f.close()
# videos = driver.find_elements_by_class_name('basicList_title__3P9Q7')
# len(videos)

# for video in videos:
#     print( video.text )


# <--------------------------워드클라우드-------------------------------------->

# import matplotlib.pyplot as plt
# from wordcloud import WordCloud

# wordcloud = WordCloud(font_path='c:/windows/fonts/gulim.ttc', background_color='white').generate(y)

# plt.figure(figsize=(22,22))
# plt.imshow(wordcloud, interpolation='lanczos') 
# plt.axis('off') 
# plt.show() 