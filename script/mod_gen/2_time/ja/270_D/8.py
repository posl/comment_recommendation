def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.reverse()
    for a in A:
        if N % a == 0:
            print(N - a)
            break
        else:
            N -= N % a

if __name__ == '__main__':
    main()