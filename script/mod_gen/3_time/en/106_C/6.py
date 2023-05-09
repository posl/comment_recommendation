def main():
    S = input()
    K = int(input())
    s = ''
    for i in range(K):
        s += S[i]
        if S[i] != '1':
            break
    if len(s) == K:
        print(S[K-1])
    else:
        print(s[0])

if __name__ == '__main__':
    main()