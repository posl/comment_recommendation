def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    # print(N, M)
    # print(AB)
    # 1.所有人都是朋友的情况
    # 2.所有人都不是朋友的情况
    # 3.其他情况
    # 1.所有人都是朋友的情况
    if M == 0:
        print(N)
