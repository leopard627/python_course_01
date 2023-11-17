'Hello World single ' # 작은따옴표

"Hello World double " # 큰 따옴표

""" Hello World!!!! tripple? """

'doesn\'t' # 작은 따옴표를 이스케이프 하려면 \ 역슬래쉬를 사용

"doesn't " # 또는 큰 따옴표 안의 작은따옴표를 쓴다, 이경우 이스케이프가 필요없다

s = 'First line.\nSecond line.' # \n은 새로운 줄(라인)을 의미한다

s = 'Py' 'thon' # 두 개 이상의 문자열 리터럴 (즉, 따옴표로 둘러싸인 것들) 가 연속해서 나타나면 자동으로 이어 붙여집니다

prefix = "Py"

prefix + "thon"

word = 'Python'

word[0] # 'P'

word[5] # 'n'

word[-1] # 마지막 문자 'n'

word[-2] # 마지막 두번째 문자 'o'

word[-6] # 'P'

word[0:2] # 'Py'

word[2:5] # 'tho' 위치 0(포함) 부터 2(제외)까지의 문자

word[:2] # 'Py' 처음부터 위치 2(제외)까지의 문자

word[4:] # 'on' 위치 4(포함)부터  끝까지의 문자

word[-2:] # 'on' 위치 두 번째(포함)부터 끝까지의 문자

word[:2] + word[2:] # 'Python'

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

# word[42] # 에러 발생!

word[42:] # 하지만 범위를 벗어나는 슬라이스 인덱스는 슬라이싱할때 부드럽게 처리 (오류 X)

# 오류 파이썬 문자열은 변경할 수 없다 — 불변 이라고 합니다.
# 그래서 문자열의 인덱스로 참조한 위치에 대입하려고 하면 에러를 일으킵니다:
# word[0] = 'J'

# 오류
# word[2:] = 'py' 

# 파이썬 3.6 부터 추가된 f 문자열 포메팅

name = "Alice"

text = f"My name is {name}"

#### 문자열 내장 라이브러리 소개

a = "abcde".upper()

a = "ABCDE".lower()

a = " hello ".strip()

a = "Python and Snake".replace("Snake", "Computer")

a = "Hello,World".split(",")

print(a)

# 나중에 여러 개발자들과 협업을 하는경우 '를 사용할지, "를 공통으로 사용할지 정해야합니다