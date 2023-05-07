def resolve():
    N = int(input())
    i = 0
    while True:
        i += 1
        N -= i
        if N <= 0:
            print(i)
            break
