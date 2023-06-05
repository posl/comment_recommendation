def judge():
    number = int(input())
    if number%10 == 7 or (number//10)%10 == 7 or (number//100)%10 == 7:
        print("是")
    else:
        print("否")
