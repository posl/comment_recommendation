def main():
    N = int(input())
    ans = 0
    for i in range(357, N+1):
        if "3" in str(i) and "5" in str(i) and "7" in str(i):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()