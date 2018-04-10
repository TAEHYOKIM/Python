#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup #BeautifulSoup 임포트
from selenium import webdriver #셀레니움 임포트
import re
import time
from urllib.request import urlopen, urlretrieve
from PIL import Image

def posterSucker(year1,year2):
    driver = webdriver.PhantomJS('/Users/hbk/data/phantomjs') #팬텀js 드라이버 경로 선언
    driver.set_page_load_timeout(30)
    mdict = {}
    for i in range(year1,year2+1):
        
        j = 1
        text = []
        while True:
            driver.get('https://movie.naver.com/movie/sdb/browsing/bmovie.nhn?year='+str(i)+'&page='+str(j))
            driver.implicitly_wait(10)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            if soup.select('#old_content > ul > li') == text:
                break
            else:
                text = soup.select('#old_content > ul > li')
                long = len(text) 
                print(str(j)+'번 페이지 영화 제목 저장 시작')
                for k in soup.select('#old_content > ul > li'): #게시판 글 중 제목과 링크의 li선택하기
                    print(str(long)+'개 남음') 
                    code = re.sub('.[\D]','',k.select_one('a').attrs['href'])
                    #딕션너리에 글번호, 영화제목 넣음.
                    mdict[code] = k.select_one('a').get_text()
                    long -= 1
                j += 1

        long2 = len(mdict.keys())
        print(str(i)+'년도 영화 포스터 파일 수집')
        img = ''
        for i in mdict.keys(): #딕셔너리에서 글번호만 뽑아 돌림
            url = 'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?code='+ str(i) #포스터 사진 사이트로 이동
            driver.get(url)
            driver.implicitly_wait(10)
            soup = BeautifulSoup(driver.page_source, 'html.parser') #소스 가져와서
            
            try:
                url1 = soup.find('img',id='targetImage')['src']
                if 
                with urlopen(url1) as f:
                    with open('/Users/hbk/data/poster/'+str(i)+'.jpg','wb') as w: # 저장위치 지정
                        img = f.read()
                        w.write(img)
                        im = Image.open('/Users/hbk/data/poster/'+str(i)+'.jpg')
                        mdict[str(i)] = [mdict[str(i)],im.size()]
                long2 -= 1
                print(long2,'개 남음')       
                 
            except TypeError:
                mdict[str(i)] = [mdict[str(i)],'none'] # 그림파일 없으면 none
                continue
            except OSError:
                # 없는 파일번호 오류발생하면 다음 키번호로 넘어가자

    driver.close()
    return mdict
posterSucker(2020,2020)                
                
                
                
######################                
                
                
                
                url1 = soup.find('img',id='targetImage')['src']
                with open('/Users/hbk/data/poster/'+i+'.jpg', 'wb') as w: #이미지 파일 저장
                    img = urlretrieve(soup.find('img',id='targetImage')['src'], i)
                    w.write(img) #포스터 파일 저장
                        im = Image.open('/Users/hbk/data/poster/' + i+'.jpg') #이미지 열기
                        mdict[str(i)] = [mdict[str(i)],im.size] #이미지 사이즈를 딕션너리에 넣어줌
            long2 -= 1
            print(str(long2)+'개 남음')
                    
        driver.close() #드라이버 닫기
    return mdict #결과물확인
suckPoster(2020,2020)
mdict

url = 'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?code=164122'
driver = webdriver.PhantomJS('/Users/hbk/data/phantomjs')
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
url1 = soup.find('#content > div.article > div.mv_info_area > div.poster > a > img')
with urlopen(soup.find('img',id='targetImage')['src']) as f:
    with open('/Users/hbk/data/poster/test.jpg','wb') as w:
        img = f.read()
        w.write(img)
soup.find('img',id='targetImage')['src']
urlretrieve(soup.find('img',id='targetImage')['src'])
Image.open('/Users/hbk/data/poster/test.jpg')
            
#content > div.article > div.mv_info_area > div.poster > a > img                   