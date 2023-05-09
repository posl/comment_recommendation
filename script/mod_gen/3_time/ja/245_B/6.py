def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = set(A)
    for i in range(N+1):
        if i not in B:
            print(i)
            break

if __name__ == '__main__':
    main()