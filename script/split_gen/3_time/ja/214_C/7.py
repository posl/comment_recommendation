def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    for i in range(n):
        print(t[i] + s[(i + 1) % n] - t[(i + 1) % n])
