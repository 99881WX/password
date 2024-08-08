t = 0
password = 'a123456'
while t < 3:
    pwd = input('請輸入密碼')
    t = t + 1
    if pwd == password:
        print('密碼正確')
        break
    else:
        print('密碼不正確')
        if t < 3:
            print('您還有',3 - t ,'次機會')
        else:
        	print('笑你被鎖帳號，再不寫起來啊lol')