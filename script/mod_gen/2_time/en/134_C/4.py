def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.sort()
    for i in range(n):
        if i == 0:
            print(a[n - 2])
        elif i == n - 1:
            print(a[n - 2])
        else:
            print(max(a[n - 2], a[i - 1]))
main()
You can check the submission here.

if __name__ == '__main__':
    main()