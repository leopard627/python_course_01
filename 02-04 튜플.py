# 튜플과 시퀀스 (시퀀스형: list, tuple, range)
# 리스트는 가변이고 튜플은 불변이다!
# 다양한 형태의 튜플

tuple1 = ()

tuple2 = (1,)

tuple3 = (1, 2, 3)

tuple4 = 1, 2, 3

tuple5 = ('a', 'b', ('ab', 'cd'))


t = 12345, 54321, 'hello!'

t[0] # 12345

t # (12345, 54321, 'hello!')

u = t, (1, 2, 3, 4, 5) # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# t[0] = 88888 # 오류 발생 - 튜플내에 새로운 값을 다시 할당할 수 없습니다

empty = ()

hello = "hello", # 뒤쪽 콤마 , 

len(empty) # 0

len(hello) # 1

hello # ('hello', )