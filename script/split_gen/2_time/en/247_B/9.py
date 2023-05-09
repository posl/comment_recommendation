def main():
    N = int(input())
    S = [input().split() for _ in range(N)]
    if len(set([s for s, _ in S])) < N and len(set([t for _, t in S])) < N:
        print("No")
    else:
        print("Yes")
