def main():
    n = int(input())
    seq = []
    for i in range(n):
        seq.append([int(x) for x in input().split()])
    print(len(set(tuple(x) for x in seq)))
