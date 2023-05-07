def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    if A == B:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()