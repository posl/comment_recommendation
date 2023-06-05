def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    x = 0
    for i in range(N):
        if A[i] > x:
            print(x)
            break
        else:
            x += 1
    else:
        print(x)

if __name__ == '__main__':
    main()