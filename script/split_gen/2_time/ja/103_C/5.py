def main():
    N = int(input())
    A = list(map(int,input().split()))
    M = max(A)
    print(sum(A)-M)
