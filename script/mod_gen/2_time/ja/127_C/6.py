def main():
    N, M = map(int, input().split())
    gates = [list(map(int, input().split())) for _ in range(M)]
    gates.sort(key=lambda x: x[1])
    ans = 0
    R = 0
    for L, R in gates:
        if L > R:
            ans = 0
            break
        if L > R:
            break
        ans += 1
        R = R
    print(ans)
    return

if __name__ == '__main__':
    main()