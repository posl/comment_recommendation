def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = sum(1/a for a in A)
    print(1/ans)
