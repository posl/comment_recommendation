def main():
    N = int(input())
    seq = []
    for i in range(N):
        seq.append(input().split())
    seq.sort()
    cnt = 1
    for i in range(N-1):
        if seq[i] != seq[i+1]:
            cnt += 1
    print(cnt)
