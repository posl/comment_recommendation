def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    for i in range(N):
        if A[i] == i:
            continue
        else:
            print(i)
            exit()
    print(N)

if __name__ == '__main__':
    main()