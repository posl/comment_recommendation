def main():
    n = int(input())
    h = list(map(int, input().split()))
    h = [0] + h
    for i in range(1, n + 1):
        if h[i] - h[i - 1] > 1:
            print("No")
            exit()
        if h[i] - h[i - 1] == 1:
            h[i] -= 1
    print("Yes")
