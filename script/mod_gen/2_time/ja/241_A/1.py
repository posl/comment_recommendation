def main():
    a = list(map(int, input().split()))
    ans = 0
    for i in range(3):
        ans = a[ans]
    print(ans)

if __name__ == '__main__':
    main()