
# 지금쯤 아마도 여러분은 대부분의 컨테이너 객체들을 for 문으로 루핑할 수 있음을 눈치챘을 것입니다:
# for 문은 컨테이너 객체에 대해 iter() 를 호출합니다. 
# 이 함수는 메서드 __next__() 를 정의하는 이터레이터 객체를 돌려주는데,
# 이 메서드는 컨테이너의 요소들을 한 번에 하나씩 액세스합니다.
# 남은 요소가 없으면, __next__() 는 StopIteration 예외를 일으켜서 for 루프에 종료를 알립니다. next() 내장 함수를 사용해서 __next__() 메서드를 호출할 수 있습니다; 이 예는 이 모든 것들이 어떻게 동작하는지 보여줍니다:

for element in [1, 2, 3]:
    print(element)

for element in (1, 2, 3):
    print(element)

for key in {'one':1, 'two':2}:
    print(key)

for char in "123":
    print(char)

for line in open("new-jeans.txt"):
    print(line, end='')


s = 'xyz'

it = iter(s)

print(next(it)) # x

print(next(it)) # y

print(next(it)) # z

# print(next(it)) # 아래와 같은 오류가 발생

#     print(next(it)) # 오류 ??
#           ^^^^^^^^
# StopIteration

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    

rev = Reverse('Python')

iter(rev)

for c in rev:
    print(c)

# n
# o
# h
# t
# y
# P

# 제너레이터는 이터레이터를 만드는 간단하고 강력한 도구입니다.
# 일반적인 함수처럼 작성되지만 값을 돌려주고 싶을 때마다 yield 문을 사용합니다.
# 제너레이터에 next() 가 호출될 때마다, 제너레이터는 떠난 곳에서 실행을 재개합니다
# (모든 데이터 값들과 어떤 문장이 마지막으로 실행되었는지 기억합니다).
# 예는 제너레이터를 사소할 정도로 쉽게 만들 수 있음을 보여줍니다:

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('Python'):
    print(char)

# n
# o
# h
# t
# y
# P