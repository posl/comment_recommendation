def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = sorted(A)
    A.append(2001)
    for i in range(2001):
        if A[i] != i:
            print(i)
            break
