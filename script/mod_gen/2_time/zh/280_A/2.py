def main():
    a,b = map(int,input().split())
    ans = 10**18
    for i in range(1,10000):
        tmp = i*b
        if tmp >= ans:
            break
        tmp += a/(i**0.5)
        if tmp < ans:
            ans = tmp
    print(ans)

if __name__ == '__main__':
    main()