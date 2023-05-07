def main():
    N = int(input())
    S = str(N)
    L = len(S)
    ans = 0
    for i in range(L):
        if i % 3 == 0 and i != 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()