def check_divisible(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    if number % sum == 0:
        print("Yes")
    else:
        print("No")
