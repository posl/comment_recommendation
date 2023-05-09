def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(min(set(range(2001)) - set(A)))
