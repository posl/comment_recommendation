def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(1, n):
        if h[i] < h[i-1]:
            h[i] += 1
        if h[i] < h[i-1]:
            print("No")
            return
    print("Yes")
