
# f = open("new-jeans.txt", "w") # 내 작업 경로에 new-jeans.txt 가 생성
# f.close()


# f = open("new-jeans.txt", "w")
# f.write("사랑합니다 뉴진스!")
# f.close()


# f = open("new-jeans.txt", "w")
# for x in range(5):
#     f.write("사랑합니다 뉴진스!\n")
# f.close()

# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!


# 작성한 파일을 읽어보자

f = open("new-jeans.txt", "r")
lines = f.readlines()

for line in lines:
    print(line.strip()) # 줄바꿈 문자 제거

# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!
# 사랑합니다 뉴진스!

f = open("new-jeans.txt", "a")
f.write("\n")
for x in range(5):
    f.write("죄송합니다 뉴진스!\n")
f.close()

# 앞에서 배운 방법대로 7파일을 쓰고 닫기
f = open("foo.txt", 'w')
f.write("파이썬 너무 재미있어요!")
f.close()

# with 문과 함께 사용해보기
with open("foo.txt", "w") as f: # 파일을 닫을 필요가 없습니다!
    f.write("파이썬 너무 재미있어요!") 
