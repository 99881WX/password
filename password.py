t = 0
password = 'a123456'
while t < 3:
    pwd = input('請輸入密碼')
    if pwd == password:
        print('密碼正確')
        break
    else:
        pwd != password
        print('密碼不正確，您還有',2 - t ,'次機會')
        t = t + 1