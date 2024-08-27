a, b = map(int, input().strip().split(' '))
print(a, '+', b,'=',a+b)

#f-string :문자열 앞에 f 접두사를 붙이고 중괄호 {} 안에 변수나 표현식을 넣는 방법
a, b = map(int, input().strip().split(' '))
print(f"{a} + {b} = {a + b}")