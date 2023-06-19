def lllk():
    k = int(input())
    num = 1
    while k > 0:
        if num % 10 == 0:
            num += 1
        elif num % 10 == 9:
            num += 2
        else:
            num += 1
        k -= 1
    print(num-1)
