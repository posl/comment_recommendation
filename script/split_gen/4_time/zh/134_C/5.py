def main():
    n = int(input())
    A = []
    for i in range(n):
        A.append(int(input()))
    for i in range(n):
        print(max(A[:i]+A[i+1:]))
