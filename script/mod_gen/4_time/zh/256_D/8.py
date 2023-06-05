def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    data.sort(key=lambda x:x[0])
    new_data = [data[0]]
    for i in range(1, n):
        if new_data[-1][1] < data[i][0]:
            new_data.append(data[i])
        elif new_data[-1][1] < data[i][1]:
            new_data[-1][1] = data[i][1]
    for i in range(len(new_data)):
        print(new_data[i][0], new_data[i][1])

if __name__ == '__main__':
    main()