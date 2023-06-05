def main():
    N, L = map(int, input().split())
    if L > 0:
        print((N-1)*L - N*(N-1)//2)
    elif L < 0:
        print((N-1)*L + N*(N-1)//2)
    else:
        print(N*L)
