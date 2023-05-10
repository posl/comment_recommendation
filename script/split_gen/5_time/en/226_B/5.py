def main():
    N = int(input())
    seq = []
    for i in range(N):
        seq.append(list(map(int, input().split())))
    seq.sort()
    prev = seq[0]
    count = 1
    for i in range(1, N):
        if seq[i] != prev:
            count += 1
            prev = seq[i]
    print(count)
