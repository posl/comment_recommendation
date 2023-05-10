def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    oven = [0, 0]
    for i in range(N):
        oven[0] += T[i]
        if oven[0] <= oven[1]:
            oven[1] = oven[0]
        else:
            oven[0] = oven[1]
    print(oven[1])
