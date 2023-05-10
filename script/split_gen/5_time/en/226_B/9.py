def main():
    N = int(input())
    seq = []
    for i in range(N):
        seq.append(input().split())
    seq.sort()
    print(len(list(k for k, _ in itertools.groupby(seq))))
