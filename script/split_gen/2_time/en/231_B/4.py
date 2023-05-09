def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    count = 1
    maxcount = 1
    maxname = S[0]
    for i in range(1,N):
        if S[i] == S[i-1]:
            count = count + 1
            if count > maxcount:
                maxcount = count
                maxname = S[i]
        else:
            count = 1
    print(maxname)
