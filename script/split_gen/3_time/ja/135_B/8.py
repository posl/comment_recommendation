def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.sort()
    if P == list(range(1, N+1)):
        print("YES")
    else:
        print("NO")
