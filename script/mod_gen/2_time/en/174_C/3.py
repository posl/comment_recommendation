def main():
    k = int(input())
    if k%2 == 0 or k%5 == 0:
        print(-1)
        return
    ans = 0
    for i in range(1,k+1):
        ans = (ans*10+7) % k
        if ans == 0:
            print(i)
            return
    print(-1)
    return

if __name__ == '__main__':
    main()