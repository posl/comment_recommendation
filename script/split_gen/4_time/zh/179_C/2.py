def problem179_c():
    N = int(input())
    count = 0
    for i in range(1, N):
        if N % i == 0:
            count += 1
    print(count)
problem179_c()
