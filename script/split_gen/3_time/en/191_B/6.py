def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(' '.join(map(str, [a for a in A if a != X])))
