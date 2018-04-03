"""
python-25일차(2018.4.3)
"""

class Person:
    def __init__(self,name): # 클래스가 인스턴스화 될 때 처음으로 호출하는 매소드
        self.name = name  # name과 self.name 다름 
    
    def say(self):
        print("내 이름은",self.name)


p1 = Person("홍길동")  # Person class의 객체 p1
p1.say()

'''
[문제 187] 생성자에 이름, 핸드폰번호, 메일, 주소 변수를 생성합니다. 
print_info 메소드를 생성한 후  출력하는 Contact 클래스를 생성하세요.
인스턴스는 set_contact 함수를 이용해서 만드시고 이름, 핸드폰번호,메일, 주소는 입력값으로 받아서 출력하세요.

이름을 입력하세요 : 홍길동

핸드폰번호를 입력하세요 : 010-1000-1004

메일을 입력하세요 : hong@aaa.com

주소를 입력하세요 : 서울시 강남구 삼성로

이름 : 홍길동 
핸드폰번호 : 010-1000-1004 
메일 : hong@aaa.com 
주소 : 서울시 강남구 삼성로
'''

class Contact:
    def set_contact(self):
        self.name = input("이름을 입력하세요 : ")
        self.phone = input("핸드폰번호를 입력하세요 : ")
        self.mail = input("메일을 입력하세요 : ")
        self.addr = input("주소를 입력하세요 : ")
        
    def print_info(self):
        print("이름 :",self.name)
        print("핸드폰번호 :",self.phone)
        print("메일 :",self.mail)
        print("주소 :",self.addr)


c = Contact()
c.set_contact()
c.print_info()




















