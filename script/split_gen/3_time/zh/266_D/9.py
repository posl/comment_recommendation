def main():
    n = int(input())
    snuke = []
    for i in range(n):
        snuke.append(list(map(int, input().split())))
    snuke.sort()
    print(snuke)
    max_size = 0
    max_size_sum = 0
    for i in range(n):
        if snuke[i][0] > max_size_sum:
            max_size_sum = snuke[i][0]
        if snuke[i][1] == 0:
            max_size += snuke[i][2]
        elif snuke[i][1] == 1:
            if max_size_sum < snuke[i][0]:
                max_size_sum = snuke[i][0]
                max_size += snuke[i][2]
        elif snuke[i][1] == 2:
            if max_size_sum < snuke[i][0]:
                max_size_sum = snuke[i][0]
                max_size += snuke[i][2]
        elif snuke[i][1] == 3:
            if max_size_sum < snuke[i][0]:
                max_size_sum = snuke[i][0]
                max_size += snuke[i][2]
        elif snuke[i][1] == 4:
            if max_size_sum < snuke[i][0]:
                max_size_sum = snuke[i][0]
                max_size += snuke[i][2]
    print(max_size)
