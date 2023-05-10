def main():
    n = int(input())
    ans = 'No'
    count = 0
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            count += 1
        else:
            count = 0
        if count >= 3:
            ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()