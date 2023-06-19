def last_card():
    N, K, A = map(int, input().split())
    if N == K:
        print(1)
    elif (K-A)%(N-A) == 0:
        print(N)
    else:
        print((K-A)%(N-A))
last_card()
