def main():
    N = int(input())
    print(N - len(set([p**e for p in range(2, int(N**0.5)+1) for e in range(2, 100) if p**e <= N])))
