def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H = [h for h in H if h >= K]
    print(len(H))
