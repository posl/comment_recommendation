def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] >= H:
        print("Yes")
    else:
        print("No")
