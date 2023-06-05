def main():
    N = int(input())
    S = input()
    rnum = S.count("R")
    gnum = S.count("G")
    bnum = S.count("B")
    count = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            if S[i] == S[j]:
                continue
            k = 2*j - i
            if k >= N:
                continue
            if S[i] == S[k] or S[j] == S[k]:
                continue
            count += 1
    print(rnum*gnum*bnum - count)
