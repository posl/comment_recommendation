def main():
    N = int(input())
    As = list(map(int, input().split()))
    mod = [0] * (10**5 + 1)
    for a in As:
        for i in range(1, a):
            mod[i] += 1
    ans = 0
    for i in range(1, 10**5 + 1):
        if mod[i] == N:
            ans += i
    print(ans)

if __name__ == '__main__':
    main()