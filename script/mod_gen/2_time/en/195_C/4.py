def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))+1):
        ans += (N//(10**(3*i)))*3
        if N%(10**(3*i)) >= 1000:
            ans += 3
        elif N%(10**(3*i)) >= 100:
            ans += 2
        elif N%(10**(3*i)) >= 10:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()