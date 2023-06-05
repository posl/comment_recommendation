def problem125_a():
    A,B,T = map(int, input().split())
    count = 0
    for i in range(T+1):
        if i%A == 0:
            count += B
    print(count)
