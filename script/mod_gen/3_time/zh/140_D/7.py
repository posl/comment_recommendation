def main():
    N, K = map(int, input().split())
    S = input()
    S = list(S)
    S.insert(0, '0')
    S.append('0')
    #print(S)
    happy = 0
    for i in range(1, N+1):
        if S[i] == 'L' and S[i-1] == 'L':
            happy += 1
        elif S[i] == 'R' and S[i+1] == 'R':
            happy += 1
    #print(happy)
    if K > happy:
        K = happy
    #print(K)
    for i in range(1, N+1):
        if S[i] == 'L' and S[i-1] == 'R':
            S[i] = 'R'
            happy += 1
        elif S[i] == 'R' and S[i+1] == 'L':
            S[i] = 'L'
            happy += 1
        if happy == K:
            break
    #print(S)
    happy = 0
    for i in range(1, N+1):
        if S[i] == 'L' and S[i-1] == 'L':
            happy += 1
        elif S[i] == 'R' and S[i+1] == 'R':
            happy += 1
    print(happy)

if __name__ == '__main__':
    main()