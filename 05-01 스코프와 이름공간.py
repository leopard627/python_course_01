def scope_test():
    def do_local():
        person = "local person"

    def do_nonlocal():
        nonlocal person
        person = "nonlocal person"

    def do_global():
        global person
        person = "global person"

    person = "test person"

    do_local()

    print(f"After local assignment: {person}")

    do_nonlocal()

    print(f"After nonlocal assignment: {person}")

    do_global()

    print(f"After global assignment: {person}")

scope_test()

print(f"In global scope: {person}")

# After local assignment: test person

# After nonlocal assignment: nonlocal person

# After global assignment: nonlocal person

# In global scope: global person

# nonlocal 대입은 scope_test 의 person 연결을 바꾸고

# global 대입은 모듈 수준의 연결을 바꿉니다.