def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    ans = []
    max_count = 0
    count = 1
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
        else:
            if max_count < count:
                ans = [S[i]]
                max_count = count
            elif max_count == count:
                ans.append(S[i])
            count = 1
    if max_count < count:
        ans = [S[N-1]]
    elif max_count == count:
        ans.append(S[N-1])
    ans.sort()
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()