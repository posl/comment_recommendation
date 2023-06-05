def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(abs(max(A)-min(A)))
