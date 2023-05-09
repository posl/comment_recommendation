def main():
    S = input()
    K = int(input())
    S = S.replace('.','0')
    S = S.replace('X','1')
    S = S.split('0')
    ans = 0
    for i in range(len(S)):
        if len(S[i]) > ans:
            ans = len(S[i])
    if ans > K:
        ans = K
    print(ans)

if __name__ == '__main__':
    main()