def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    count = 0
    max_count = 0
    max_name = S[0]
    for i in range(N):
        if S[i] == max_name:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_name = S[i-1]
            count = 1
    if count > max_count:
        max_count = count
        max_name = S[N-1]
    print(max_name)
