def solve():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    max_count = 0
    max_word = ''
    count = 0
    for i in range(N):
        if i == 0:
            count = 1
        else:
            if S[i] == S[i-1]:
                count += 1
            else:
                count = 1
        if count > max_count:
            max_count = count
            max_word = S[i]
    print(max_word)

if __name__ == '__main__':
    solve()