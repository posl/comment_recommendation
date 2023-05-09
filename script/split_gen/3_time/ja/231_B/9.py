def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = sorted(S)
    #print(S)
    max = 0
    max_name = S[0]
    count = 0
    for i in range(N):
        if S[i] == S[i-1]:
            count += 1
            if count > max:
                max = count
                max_name = S[i]
        else:
            count = 0
    print(max_name)
    return
