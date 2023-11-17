# 집합 
# 집합은 중복되는 요소가 없는 순서 없는 컬렉션입니다
# 집합을 만들 때는 중괄호나 set() 함수를 사용할 수 있습니다

lang = {'python', 'rust', 'java', 'solidity', 'perl'}

# print(lang)

"python" in lang # true 

"korean" in lang # false

a = set('qwer') # {'q', 'w', 'e', 'r'}

b = set('aqwerxkz') # {'a', 'q', 'w', 'e', 'r', 'x', 'k', 'z'}

print(a) # {'q', 'w', 'r', 'e'}

print(b) # {'q', 'r', 'k', 'x', 'w', 'a', 'z', 'e'}

print(a - b) # set() nothing

print(b - a) # {'z', 'a', 'k', 'x'}

print(a | b) # {'q', 'r', 'k', 'x', 'w', 'a', 'z', 'e'}

print(a & b) # {'q', 'w', 'r', 'e'}

