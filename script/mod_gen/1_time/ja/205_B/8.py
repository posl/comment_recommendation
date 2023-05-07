def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = list(range(1, N+1))
    if A == B:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()