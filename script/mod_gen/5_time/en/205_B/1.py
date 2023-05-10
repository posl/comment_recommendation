def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] != i+1:
            print("No")
            exit()
    print("Yes")
main()

if __name__ == '__main__':
    main()