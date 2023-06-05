def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke.append([t, x, a])
    snuke.sort()
    #print(snuke)
    max_size = 0
    for i in range(n):
        if snuke[i][0] - snuke[i][1] >= 0:
            max_size += snuke[i][2]
    print(max_size)
