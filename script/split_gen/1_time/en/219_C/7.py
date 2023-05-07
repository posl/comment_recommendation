def main():
    # read the input
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    # sort the names
    S.sort(key=lambda s: [X.index(c) for c in s])
    # print the sorted names
    for s in S:
        print(s)
