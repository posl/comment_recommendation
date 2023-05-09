def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    count = 0
    while X != 1:
        X = A[X]
        count += 1
    print(count)
