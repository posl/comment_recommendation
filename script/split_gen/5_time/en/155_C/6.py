def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    max_count = 0
    max_str = ''
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
            max_str = S[i]
    print(max_str)
