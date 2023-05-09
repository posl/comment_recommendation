def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(1, N+1):
        print(A.index(A.index(i)+1)+1)
