def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    min = max(A)
    max = min(B)
    if min <= max:
        print(max - min + 1)
    else:
        print(0)
