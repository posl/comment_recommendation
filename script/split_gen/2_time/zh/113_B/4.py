def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h = [t - i * 0.006 for i in h]
    # print(h)
    # print([abs(i - a) for i in h])
    print([abs(i - a) for i in h].index(min([abs(i - a) for i in h])) + 1)
