# for + range + pass 

words = ['python', 'java', 'perl', 'swift']

for w in words:
    print(w, len(w))

# python 6
# java 4
# perl 4
# swift 5

person = {"name": '김파이썬', "email": "abc@mail.com", "mobile": "0101111111"}

for key, value in person.items():
    print(f"{key}: {value}")

# name: 김파이썬
# email: abc@mail.com
# mobile: 0101111111

for i in range(10):
    print(i)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

print(list(range(0, 10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(0, 10, 3))) # [0, 3, 6, 9]

a = ["안녕하세요", "저는", "파이썬을", "좋아합니다"]

for i in range(len(a)):
    print(i, a[i])

# 0 안녕하세요
# 1 저는
# 2 파이썬을
# 3 좋아합니다

print(range(0, 10)) # range(0, 10)
# 이터레이트할 때 원하는 시퀀스 항목들을 순서대로 돌려주는 객체이지만, 실제로 리스트를 만들지 않아서 공간을 절약합니다.

print(sum(range(0, 10))) # 45



# loop, break, continue 그리고 else

for x in range(10):
    if x == 5:
        break;
    else:
        print(x)

# 0
# 1
# 2
# 3
# 4

for x in range(10):
    if x == 5:
        continue;
    else:
        print(x)
# 0
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9

for x in range(5):
    pass
    print(x)

# 0
# 1
# 2
# 3
# 4

if True:
    pass

# 아무일도 안생김..

def func():
    pass

class MyClass:
    pass

# 최소한의 클래스를 만들 때 흔히 사용됩니다



####
# match statments 매치 상태
a = 101

match a:
    case 100:
        print("백!")
    case 101:
        print("백하나!")
    case 102:
        print("백둘!")

# 백하나!

if a > 100:
    match a:
        case 100:
            print("100!")
        case 101:
            print("101!")
        case 102:
            print("102!")

# 101!

# Enum을 사용해서 더 깔끔하게 사용가능!

from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color("red")

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
