def main():
    N, M = map(int, input().split())
    count = 0
    for i in range(N):
        K, *A = map(int, input().split())
        if len(set(A)) == len(A):
            count += 1
    print(count)
