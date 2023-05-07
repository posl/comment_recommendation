def main():
    A, B, X = map(int, input().split())
    minN = 0
    maxN = 10**9
    while maxN - minN > 1:
        midN = (maxN + minN) // 2
        if A * midN + B * len(str(midN)) <= X:
            minN = midN
        else:
            maxN = midN
    print(minN)
