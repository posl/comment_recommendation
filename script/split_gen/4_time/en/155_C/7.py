def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    max_count = 0
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        elif S[i] == S[i-1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 1
    if count > max_count:
        max_count = count
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        elif S[i] == S[i-1]:
            count += 1
        else:
            if count == max_count:
                print(S[i-1])
            count = 1
    if count == max_count:
        print(S[i-1])
