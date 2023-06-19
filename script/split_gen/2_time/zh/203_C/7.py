def main():
    N, K = map(int, input().split())
    # 朋友村庄
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    # print(AB)
    # 朋友村庄到达的最大村庄
    max_village = 0
    # 朋友村庄的朋友村庄
    AB2 = []
    for i in range(N):
        if AB[i][0] > max_village + 1:
            break
        # 朋友村庄的朋友村庄
        AB2.append(AB[i])
        max_village = max(max_village, AB[i][0] + AB[i][1])
    # print(AB2)
    # 朋友村庄的朋友村庄的朋友村庄
    AB3 = []
    for i in range(len(AB2)):
        if AB2[i][0] > max_village + 1:
            break
        # 朋友村庄的朋友村庄的朋友村庄
        AB3.append(AB2[i])
        max_village = max(max_village, AB2[i][0] + AB2[i][1])
    # print(AB3)
    # 朋友村庄的朋友村庄的朋友村庄的朋友村庄
    AB4 = []
    for i in range(len(AB3)):
        if AB3[i][0] > max_village + 1:
            break
        # 朋友村庄的朋友村庄的朋友村庄的朋友村庄
        AB4.append(AB3[i])
        max_village = max(max_village, AB3[i][0] + AB3[i][1])
    # print(AB4)
    # 朋友村庄的朋友村庄的朋友村庄的朋友村庄的朋友村庄
    AB
