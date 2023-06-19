def main():
    N = int(input())
    A = input().split()
    A = [int(i) for i in A]
    A.sort()
    i = 0
    while i < N:
        if i != A[i]:
            print(i)
            break
        i = i + 1
    if i == N:
        print(i)
