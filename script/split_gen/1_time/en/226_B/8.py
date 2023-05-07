def main():
    N = int(input())
    seq = []
    for i in range(N):
        seq.append(input().split())
    seq.sort(key=lambda x: x[0])
    seq.sort(key=lambda x: x[1:])
    ans = 1
    for i in range(1, N):
        if seq[i-1] != seq[i]:
            ans += 1
    print(ans)
