def main():
    N = int(input())
    num = 1
    for i in range(1,N+1):
        num *= i
    ans = 0
    for i in range(1,num+1):
        if num % i == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()