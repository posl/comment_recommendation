def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in b:
        if a[i-1] == max(a):
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()