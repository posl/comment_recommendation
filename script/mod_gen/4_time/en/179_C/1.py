def main():
    n = int(input())
    ans = 0
    for a in range(1, n):
        for b in range(1, n):
            if a * b >= n:
                break
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()