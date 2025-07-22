a=eval(input())
b=eval(input())
if b > a:
    print(f"{b}比{a}大{b-a}")
elif b == a:
    print(f"{b}跟{a}一樣大")
else:
    print(f"{b}比{a}小{a-b}")