def main():
    a, b, k = map(int, input().split())
    ans = ''
    for i in range(a):
        ans += 'a'
    for i in range(b):
        ans += 'b'
    print(ans)
    for i in range(k-1):
        ans = next(ans)
        print(ans)
    print(ans)

if __name__ == '__main__':
    main()