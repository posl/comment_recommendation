def main():
    N = int(input())
    A = list(map(int, input().split()))
    min1 = min(A)
    min2 = min(filter(lambda x: x != min1, A))
    print(A.index(min2) + 1)
