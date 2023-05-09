def main():
    S = input()
    Q = S.count('?')
    S = S.replace('?','{}')
    S = S.format('A','B','C')
    S = S.replace('{}','?')
    S = S.replace('A','0')
    S = S.replace('B','1')
    S = S.replace('C','2')
    S = S.replace('?','3')
    S = S[::-1]
    ans = 0
    for i in range(len(S)):
        if S[i] == '3':
            ans += pow(3,i,Q)
    ans = ans % (10**9+7)
    print(ans)

if __name__ == '__main__':
    main()