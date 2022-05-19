for num in range(1, 101):
    string = ''

    # numが15の倍数であるときにstringに"FizzBuzz"を代入
    if num%15==0:
        string="FizzBuzz"
    # numが3の倍数であるときにstringに"Fizz"を代入
    elif num%3==0:
        string="Fizz"
    # numが5の倍数であるときにstringに"Buzz"を代入
    elif num%5==0:
        string="Buzz"
    # 上記以外のときににstringにnumの値をstring型にして代入
    else:
        string=str(num)

    # stringを出力    
    print(string)