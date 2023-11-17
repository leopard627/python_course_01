
def func():
    print("나는 함수입니다")

func() # "나는 함수입니다"


def add(a, b): # a, b는 매개변수
    return a + b # 리턴값

a = add(1, 2)

print(a) # 3

def add_more(*args):
    print(args) # (1, 2, 3, 4, 5)

add_more(1, 2, 3, 4, 5)

def add_more_with_return(*args):
    return args

tuple = add_more_with_return(1, 2, 3, 4, 5) # (1, 2, 3, 4, 5)

print(tuple)

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name="Python", email="python@mail.com") # {'name': 'Python', 'email': 'python@mail.com'}

def add_and_mul(a, b):
    return a + b, a * b

result = add_and_mul(4, 5) # (9, 20)

print(result) # (9, 20)

res1, res2 = add_and_mul(4, 5) # 9, 20

print(res1, res2)

def say(say="Hello World"):
    print(say)

say() # Hello World

say("Something!") # Something!

say(say="SomeThing!") # Something!