def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(360 - (sum(A) - N * 180))
