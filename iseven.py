a = int(input())
if a % 2 == 0 :
    print(a,"is even")
else :
    print(a,"is odd")


# f string
n = int(input())
print(f"{n} is odd" if n % 2 else f"{n} is even")