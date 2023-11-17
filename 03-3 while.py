
condition = True

a = 1

while condition:
    print(a)
    
    if a == 5:
        break
    else:
        a += 1 # a = a + 1

# 1
# 2
# 3
# 4
# 5

while True:
    print("Ctrl + C를 눌러서 while loop를 빠져나갈 수 있습니다")

# Ctrl + C를 눌러서 while loop를 빠져나갈 수 있습니다
# Ctrl + C를 눌러서 while loop를 빠져나갈 수 있습니다
# Ctrl + C를 눌러서 while loop를 빠져나갈 수 있습니다
# Ctrl + C를 눌러서 while loop를 �^C��니다
# Traceback (most recent call last):
#   File "/Users/alpsoft/Projects/Private/alpcampus_courses/python_courses/03-3 while.py", line 21, in <module>
#     print("Ctrl + C를 눌러서 while loop를 빠져나갈 수 있습니다")
# KeyboardInterrupt