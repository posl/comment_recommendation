def main():
    N = int(input())
    ans = 0
    for i in range(2,int(N**0.5)+1):
        x = i*i
        while x <= N:
            ans += 1
            x *= i
    print(N-ans)

if __name__ == '__main__':
    main()