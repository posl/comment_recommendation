def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    max_count = 0
    count = 0
    for i in range(1, N):
        if S[i] == S[i - 1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    count = 0
    for i in range(1, N):
        if S[i] == S[i - 1]:
            count += 1
        else:
            if count == max_count:
                print(S[i - 1])
            count = 0
    if count == max_count:
        print(S[i - 1])
