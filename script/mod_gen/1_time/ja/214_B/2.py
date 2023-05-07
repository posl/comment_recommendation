def main():
    S, T = map(int, input().split())
    ans = 0
    for a in range(S+1):
        for b in range(S+1-a):
            c = S - a - b
            if a * b * c <= T:
                ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()