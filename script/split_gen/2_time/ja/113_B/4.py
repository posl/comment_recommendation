def main():
    n = int(input())
    t, a = list(map(int, input().split()))
    h = list(map(int, input().split()))
    h = [abs(a - (t - i * 0.006)) for i in h]
    print(h.index(min(h)) + 1)
