def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke.append([t, x, a])
    #print(snuke)
    #snuke.sort(key=lambda x: x[0])
    #print(snuke)
    #snuke.sort(key=lambda x: x[1])
    #print(snuke)
    #snuke.sort(key=lambda x: x[2])
    #print(snuke)
    time = 0
    sum = 0
    for i in range(n):
        if snuke[i][0] >= snuke[i][1] + time:
            sum = sum + snuke[i][2]
            time = snuke[i][0]
            #print("sum = ", sum)
            #print("time = ", time)
    print(sum)

if __name__ == '__main__':
    main()