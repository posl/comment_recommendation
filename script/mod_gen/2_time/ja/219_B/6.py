def main():
    S = [input() for _ in range(3)]
    T = input()
    ans = ""
    for t in T:
        ans += S[int(t)-1]
    print(ans)

if __name__ == '__main__':
    main()