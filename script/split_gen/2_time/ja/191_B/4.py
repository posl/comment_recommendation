def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a for a in A if a != X]
    print(*A, sep=" ")
