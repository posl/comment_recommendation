def main():
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    ans = ""
    while True:
        if K == 1:
            ans += "".join(S)
            break
        else:
            ans += S.pop(0)
            K -= 1
    print(ans)

if __name__ == '__main__':
    main()