def main():
    N = int(input())
    A = list(map(int, input().split()))
    if sum(A) <= 0:
        print(0)
    else:
        print(sum(A) - min([a for a in A if a < 0]))
