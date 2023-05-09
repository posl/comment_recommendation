def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    P = 0
    for i in A:
        P += i//2
    print(P)
