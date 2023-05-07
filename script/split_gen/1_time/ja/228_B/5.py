def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i-1 for i in A]
    count = 0
    a = X-1
    while True:
        a = A[a]
        count += 1
        if a == X-1:
            break
    print(count)
