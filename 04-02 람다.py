# 람다 함수 -> 익명함수
# 예시
def add(x, y):
    return x + y

print(add(4, 5)) # 9

lambda_add = lambda x, y: x + y

print(lambda_add(4, 5)) # 9