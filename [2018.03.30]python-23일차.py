"""
python-23일차(2018.3.30)
"""

## 22-1. KoNLPy
http://konlpy-ko.readthedocs.io/ko/v0.4.3/

# 설치
'''
1. http://www.oracle.com/technetwork/java/javase/downloads/index.html (오라클)
   jdk 설치 (10 version)
2. JAVA_HOME 설정
   terminal 접속
   cd / Library/Java/JavaVirtualMachines
   ls (jdk version 확인)
   cd / Library/Java/JavaVirtualMachines/jdk-10.jdk/Contens/Home
   vi ~/.bash_profile (i or a)
   export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-10.jdk/Contens/Home (이거 입력)
   esc - :wq (저장하고 나가기)   
3. xpad 설치
   xcode-select --install
4. pip install konlpy
5. pip3 install JPype1-py3
6. pip3 uninstall JPype1-py3
7. spyder 재시작
'''


from konlpy.tag import Twitter
'''트위터 분석기
- 빅데이터 등에서 간단한 한국어 처리를 통해 색인어를 추출하는 데에 있음. 
  (단, 완전한 수준의 형태소 분석을 지향하지는 않는다.)
  
- 특징 : normalization, tokenization, stemming, phrase extraction

* 정규화 normalization (입니닼ㅋㅋ -> 입니다 ㅋㅋ, 샤릉해 -> 사랑해)
   한국어를 처리하는 예시입니닼ㅋㅋㅋㅋㅋ -> 한국어를 처리하는 예시입니다 ㅋㅋ

* 토큰화 tokenization
   한국어를 처리하는 예시입니다 ㅋㅋ 
   -> 한국어Noun, 를Josa, 처리Noun, 하는Verb, 예시Noun, 입Adjective, 니다Eomi ㅋㅋKoreanParticle

* 어근화 stemming (입니다 -> 이다)
   한국어를 처리하는 예시입니다 ㅋㅋ 
   -> 한국어Noun, 를Josa, 처리Noun, 하다Verb, 예시Noun, 이다Adjective, ㅋㅋKoreanParticle

* 어구 추출 phrase extraction
   한국어를 처리하는 예시입니다 ㅋㅋ -> 한국어, 처리, 예시, 처리하는 예시
'''

t = Twitter()
text = t.pos("아버지가방에들어가신다",norm=True,stem=True)
text = t.sentences("아버지가방에들어가신다",norm=True,stem=True)
text
# norm : "그래욕 ㅋㅋㅋ" -> 그래요
# stem : "그렇다" 원형을 찾아 준다.


from konlpy.tag import Kkma
k = Kkma()
txt = "통찰력은 사물이나 현상의 원인과 결과를 이해하고 간파하는 능력이다. 통찰력을 얻는 좋은 방법은 독서이다."

# 문장을 분석
k.sentences(txt)

# 명사분석
k.nouns(txt)

# 형태소 분석
k.pos(txt)


from konlpy.tag import Hannanum
h = Hannanum()
h.nouns(txt)


from konlpy.tag import Twitter
t = Twitter()
t.nouns(txt)
t.pos(txt)


import nltk 
from konlpy.corpus import kobill
file_ko = kobill.fileids()


# 문재인 대통령 취임사 분석
# kobill 검색 - 폴더찾아가기 - 문재인 연설 복붙 (여기서 window 파일 그대로 받으면 오류)
doc_ko = kobill.open("moon.txt").read()
doc_ko # 문서 내용 확인하기



from konlpy.tag import Twitter
t = Twitter()
tokens_ko = t.nouns(doc_ko)  # 명사
tokens_ko

ko = nltk.Text(tokens_ko)
len(ko.tokens)
len(set(ko.tokens))
ko.vocab()


import matplotlib
import matplotlib.pyplot as plt
#from matplotlib import font_manager, rc
#font_name = font_manager.FontProperties
#(fname = "c:/Windows/Fonts/malgun.ttf").get_name()
#rc('font',family = font_name)

from matplotlib import rc #한글설정 1
rc('font', family='AppleGothic') #한글설정 2
plt.rcParams['axes.unicode_minus'] = False #한글설정 3


plt.figure(figsize = (12,6))
ko.plot(50)
plt.show()


stopword = ['.', ',', '(',')', '의', '에', '해', '제']
stopword


ko = [word for word in ko if word not in stopword]

ko = nltk.Text(ko)
len(ko.tokens)
len(set(ko.tokens))
ko.vocab()


plt.figure(figsize = (12,6))
ko.plot(50)
plt.show()


ko.count("국민")  # '국민'이 언급된 횟수
ko.concordance("약속")  # '약속' 주변 단어들
ko.collocations()  # 연이어 발생되는 단어들

# 오류 발생시

nltk.download('stopwords')
#스파이더에서 이거 실행시키면 됨

nltk.download('stopwords')
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\stu\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping corpora\stopwords.zip.
Out[66]: True


아나콘다 프롬프트 들어가서
import nltk
nltk.download()

all 다운로드 하기


from nltk import collocations
from konlpy.utils import pprint
measures = collocations.BigramAssocMeasures()
finder = collocations.BigramCollocationFinder.from_words(ko)
pprint(finder.nbest(measures.pmi,10))




# 연어찾기
http://konlpy-ko.readthedocs.io/ko/v0.4.3/examples/collocations/



