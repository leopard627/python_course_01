squares = [1, 4, 9, 16, 25]

squares[0] # '1' 첫번째 아이템을 리턴합니다 

squares[-1] # 25 제일 마지막 아이템을 리턴합니다

squares[-3:] # 새 리스트를 반환합니다 [9, 16, 25]

squares[:] # 모든 슬라이스 연산 => 새 리스트를 리턴합니다 (새로운 얕은 복사)

squares + [36, 49, 64, 81, 100] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 

# 불변인 문자열과는 다르게 리스트는 *가변* 입니다. 내용을 변경할 수 있습니다.

my_list = [1, 2, 3, 4]

my_list[1] = 99

my_list.append(5) # 리스트의 맨 뒤에 새로운 값을 추가할 수 있습니ㄷ

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters[2:5] = ['C', 'D', 'E'] # 슬라이스에 대입하여 값을 바꿀 수 있습니다 ['a', 'b', 'C', 'D', 'E', 'f', 'g']

letters[2:5] = [] # ['a', 'b', 'f', 'g']

letters = ['a', 'b', 'c', 'd'] # 내장함수 len() 을 통해서 리스트의 길이를 가져올 수 있습니다

len(letters)

a = ['a', 'b', 'c']

n = [1, 2, 3]

x = [a, n] # 리스트를 중첩 시킬수 있습니다

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple') # 2

fruits.count('wow') # 0 없음

fruits.index('banana') # 3

fruits.reverse() # 역순으로 값을 반환

fruits.append('한라봉')

fruits.sort()

# 리스트를 스택으로 사용해보기

stack = [3, 4, 5]

stack.append(6)

stack.append(7) # [3, 4, 5, 6, 7]

stack.pop() # 7

stack.pop() # 6

stack.pop() # 5

stack # [3, 4]

# 리스트를 큐로 사용해보기

from collections import deque

queue = deque(["python", "java", "kotlin"])

queue.append("perl") 

queue.append("rust") 

queue.popleft() # python

queue.popleft() # java

queue # [kotlin, perl, rust]
