def main():
    N = int(input())
    A = input().split()
    if len(set(A)) == N:
        print("YES")
    else:
        print("NO")
