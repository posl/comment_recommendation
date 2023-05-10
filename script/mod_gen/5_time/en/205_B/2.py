def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if A[i] != i+1:
            print("No")
            break
    else:
        print("Yes")

if __name__ == '__main__':
    main()