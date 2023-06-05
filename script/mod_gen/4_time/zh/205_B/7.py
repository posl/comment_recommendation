def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n+1):
        if i != a[i-1]:
            print("No")
            break
    else:
        print("Yes")

if __name__ == '__main__':
    main()