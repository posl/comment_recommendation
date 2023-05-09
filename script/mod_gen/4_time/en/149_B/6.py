def main():
    A,B,K = map(int,input().split())
    if A >= K:
        A = A - K
    else:
        K = K - A
        A = 0
        if B >= K:
            B = B - K
        else:
            B = 0
    print(A,B)
    return

if __name__ == '__main__':
    main()