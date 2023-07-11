def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    if len(set(A)) == N:
        print("YES")
    else:
        print("NO")
