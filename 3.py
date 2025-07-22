# 1.加入例外處理 try+except Exception as e
# 2.重複輸入，直到a=>exit 離開

while True:
    try:
        a=input("請輸入a:")
        if a == 'exit':
            break
        a = eval(a)
        b=eval(input("請輸入b:"))
        if b > a:
            print(f"{b}比{a}大{b-a}")
        elif b == a:
            print(f"{b}跟{a}一樣大")
        else:
            print(f"{b}比{a}小{a-b}") 
            
    except Exception as e:
        print(f"輸入錯誤: {e}")