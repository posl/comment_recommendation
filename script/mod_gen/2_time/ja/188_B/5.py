def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = [a[i]*b[i] for i in range(n)]
    if sum(ab) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()