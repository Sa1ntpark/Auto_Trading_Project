import re

#re.compile()를 통해 정규표현식을 컴파일 하여 변수에 저장한 후 사용가능
p = re.compile('[a-z]+')#알파벳 소문자가 1부터 여러개까지를 의미
m = p.match('python')
# print(m)
# print(m.group())

#match함수는 시작 부분부터 일치 패턴을 찾아서 'Use python'와 매치가 안됨
m = p.match('Use python')
#print(m)
#print(m.group()) None

p = re.compile('[가-힣]+')
m = p.match('파이썬')
#print(m)

p = re.compile('[a-z]+')
m = p.search('Use python')
#print(m)

p = re.compile('[a-zA-Z]+')
m = p.findall('Life is too short, You need Python.')
#print(type(m))
# for i in m:
#     print(i)

p = re.compile('[a-zA-Z]+')
m = p.finditer('Life is too short, You need Python.')
#반복 가능한 객체(iterator object)를 반환

for i in m:
    print(i)


# str1 = '오늘 2022a12a23 이다'

# p = re.compile('[0-9]+.[0-9]+.[0-9]+')
# m = p.findall(str1)
#print("--------")
#print(m)
#print("--------")

# p = re.compile('[0-9]+')
# m = p.findall(str1)
# print("--------")
# print(m)
# m = ''.join(m) # 공백이 없이 합쳐라
# print(m)
# print("--------")
