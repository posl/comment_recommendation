def main():
    N = int(input())
    A = list(map(int, input().split()))
    if sum(A) <= 0:
        print(0)
        return
    else:
        print(sum(A) - min(A))
