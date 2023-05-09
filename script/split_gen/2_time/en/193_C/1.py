def main():
    N = int(input())
    print(N - 1 - len(set([a**b for a in range(2, int(N**0.5)+1) for b in range(2, int(N**0.5)+1)])))
