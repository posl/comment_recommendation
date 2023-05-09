def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A_ = [a for a in A if a != X]
    print(*A_)
