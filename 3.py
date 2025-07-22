# 1.加入例外處理 try+except Exception as e
# 2.重複輸入，直到a=>exit 離開

while True:
    try:
        a=input("請輸入a(exit:離開):")
        # 判斷離開條件
        if a == 'exit':
            break
        # 轉換成數值
        a = eval(a)
        b=eval(input("請輸入b:"))
        # 判斷大小
        if b > a:
            print(f"{b}比{a}大{b-a}")
        elif b == a:
            print(f"{b}跟{a}一樣大")
        else:
            print(f"{b}比{a}小{a-b}") 
            
    except Exception as e:
        print(f"輸入錯誤: {e}")