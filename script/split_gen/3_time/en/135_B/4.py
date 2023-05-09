def main():
    N = int(input())
    p = list(map(int, input().split()))
    if p == sorted(p):
        print("YES")
    elif p[0] == 1 or p[-1] == N:
        print("NO")
    elif p[0] == N and p[-1] == 1:
        print("YES")
    else:
        print("NO")
