def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    count = 1
    max_count = 0
    ans = []
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
        else:
            if max_count < count:
                ans = []
                ans.append(S[i])
                max_count = count
                count = 1
            elif max_count == count:
                ans.append(S[i])
                count = 1
            else:
                count = 1
    if max_count < count:
        ans = []
        ans.append(S[N-1])
        max_count = count
    elif max_count == count:
        ans.append(S[N-1])
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()