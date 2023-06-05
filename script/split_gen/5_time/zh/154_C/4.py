def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(n-1):
        if A[i] == A[i+1]:
            print("NO")
            return
    print("YES")
