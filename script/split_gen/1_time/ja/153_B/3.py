def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if H > A[-1]:
        print("No")
    else:
        print("Yes")
