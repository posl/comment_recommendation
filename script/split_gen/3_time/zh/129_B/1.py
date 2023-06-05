def main():
    n = int(input())
    w = list(map(int, input().split()))
    w.sort()
    w1 = w[:n//2]
    w2 = w[n//2:]
    print(abs(sum(w1) - sum(w2)))
