def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i == 0:
            ans += p[i] / 2
        else:
            ans += p[i]
    print(int(ans))

if __name__ == '__main__':
    main()