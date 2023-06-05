def main():
    N = int(input())
    T = [int(i) for i in input().split()]
    T.sort()
    oven = [0] * 2
    for i in range(N):
        oven[0] += T.pop()
        oven.sort()
    print(oven[1])
