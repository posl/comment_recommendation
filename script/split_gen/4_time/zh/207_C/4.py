def main():
    N = int(input())
    tlr_list = []
    for i in range(N):
        tlr_list.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr_list[i][2] >= tlr_list[j][1] and tlr_list[i][1] <= tlr_list[j][2]:
                count += 1
    print(count)
