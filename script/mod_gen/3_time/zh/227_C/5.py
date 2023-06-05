def main():
    N = int(input())
    ans = 0
    for a in range(1, N + 1):
        for b in range(a, N + 1):
            if a * b > N:
                break
            for c in range(b, N + 1):
                if a * b * c > N:
                    break
                if a == b and b == c:
                    ans += 1
                elif a == b or b == c:
                    ans += 3
                else:
                    ans += 6
    print(ans)

if __name__ == '__main__':
    main()