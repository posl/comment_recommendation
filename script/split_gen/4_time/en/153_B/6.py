def main():
    h, n = map(int, input().split())
    arr = list(map(int, input().split()))
    if h <= sum(arr):
        print("Yes")
    else:
        print("No")
