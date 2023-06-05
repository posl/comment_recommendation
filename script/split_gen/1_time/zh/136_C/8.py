def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(1, n):
        if h[i] - h[i - 1] >= 2:
            print("No")
            return
    print("Yes")
