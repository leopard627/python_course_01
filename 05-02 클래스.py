
class ClassName:
    pass


class MyClass:
    """ A Simple example class """

    i = "abcde"

    def f(self):
        return "안녕하세요?"
    
x = MyClass() # 클래스의 새 인스턴스 를 만들고 이 객체를 지역 변수 x 에 대입합니다.

print(x.f())

class MySecondClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(self.x, self.y)

c = MySecondClass(1, 2)

# print(c.x, c.y)

# print(c)

c.display()

c.x = 999 # ?

# print(c.x)

class Person:
    friends = []

    def __init__(self, name):
        self.name = name

    def make_friends(self, name):
        self.friends.append(name)

    def show_friends(self):
        print(self.friends)
    
a = Person("daniel")

b = Person("alice")

a.make_friends("jay")

b.make_friends("piona")

a.show_friends() # ['jay', 'piona']

b.show_friends() # ['jay', 'piona']

# 코드를 수정합니다

class PersonV2:

    def __init__(self, name):
        self.name = name
        self.friends = []

    def make_friends(self, name):
        self.friends.append(name)

    def show_friends(self):
        print(self.friends)

a = PersonV2("daniel")

b = PersonV2("alice")

a.make_friends("jay")

b.make_friends("piona")

a.show_friends() # ['jay', 'piona']

b.show_friends() # ['jay', 'piona']

### 상속

class PersonV3(PersonV2):

    def show_friends(self):
        print("???????")

a = PersonV3("henry")

a.make_friends("diana")

a.make_friends("jay")

a.show_friends()
