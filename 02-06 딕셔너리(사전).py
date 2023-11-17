person = {'name': "jihun", 'mobile': "01011112222", "email": "ali@email.xxx"}

person["email"] = "abc@email.com"

person["mobile"] = "07011122222"

print(person) # {'name': 'jihun', 'mobile': '07011122222', 'email': 'abc@email.com'}

del person["email"]

print(person) # {'name': 'jihun', 'mobile': '07011122222'}

print(list(person)) # ['name', 'mobile']

print(sorted(person)) # ['mobile', 'name']

"mobile" in person

"wallet" in person

# dict() 생성자는 키-값 쌍들의 시퀀스로 부터 직접 딕셔너리를 구성합니다.
