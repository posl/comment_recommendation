def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    avg = [T - h * 0.006 for h in H]
    diff = [abs(a - av) for a, av in zip([A] * N, avg)]
    print(diff.index(min(diff)) + 1)
