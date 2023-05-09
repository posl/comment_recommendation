def main():
    N = int(input())
    A = list(map(int, input().split()))
    counter = {}
    for a in A:
        if a not in counter:
            counter[a] = 0
        counter[a] += 1
    for i in range(N):
        if A[i] in counter:
            print(N - counter[A[i]])
        else:
            print(N - 1)
