def main():
    N,X = map(int,input().split())
    S = input()
    score = X
    for i in range(N):
        if S[i] == 'o':
            score += 1
        else:
            if score > 0:
                score -= 1
    print(score)

if __name__ == '__main__':
    main()