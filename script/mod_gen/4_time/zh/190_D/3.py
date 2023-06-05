def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            m = N//i
            if m%2 == i%2:
                ans += 1
    print(ans*2)

if __name__ == '__main__':
    main()