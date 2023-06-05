def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == [i for i in range(1, n+1)]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()