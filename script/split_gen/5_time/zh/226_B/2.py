def main():
    n = int(input())
    seqs = []
    for i in range(n):
        seqs.append(list(map(int,input().split()))[1:])
    seqs.sort()
    ans = 1
    for i in range(1,n):
        if seqs[i] != seqs[i-1]:
            ans += 1
    print(ans)
