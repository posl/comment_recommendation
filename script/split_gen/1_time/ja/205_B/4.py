def main():
    N = int(input())
    A = list(map(int, input().split()))
    if A == sorted(A):
        print("Yes")
    else:
        print("No")
