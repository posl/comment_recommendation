def main():
    N = int(input())
    seq = []
    for i in range(N):
        seq.append(list(map(int, input().split()))[1:])
    print(len(set(map(tuple, seq))))
