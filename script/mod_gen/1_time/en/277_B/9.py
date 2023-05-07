def main():
    #input
    N = int(input())
    S = [input() for _ in range(N)]
    #print(N)
    #print(S)
    #count
    count = 0
    for i in range(N):
        if S[i][0] in 'HDCK' and S[i][1] in 'A23456789TJQK':
            count += 1
    #print(count)
    #judge
    if count == N and len(S) == len(set(S)):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()