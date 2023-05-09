def main():
    N = int(input())
    A = list(map(int, input().split()))
    A2 = sorted(A)
    print(A.index(A2[-2])+1)
