def main():
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    K -= 1
    for i in range(len(S)):
        if K == 0:
            break
        K = K // (len(S)-1-i)
    print(S[i], end='')
    S.remove(S[i])
    for i in range(len(S)):
        print(S[i], end='')

if __name__ == '__main__':
    main()