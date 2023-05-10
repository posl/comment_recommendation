def main():
    N = int(input())
    data = []
    for i in range(N):
        t, l, r = map(int, input().split())
        data.append((t, l, r))
    #print(data)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if data[i][1] <= data[j][1] and data[j][1] <= data[i][2]:
                count += 1
            elif data[i][1] <= data[j][2] and data[j][2] <= data[i][2]:
                count += 1
            elif data[j][1] <= data[i][1] and data[i][1] <= data[j][2]:
                count += 1
            elif data[j][1] <= data[i][2] and data[i][2] <= data[j][2]:
                count += 1
    print(count)
