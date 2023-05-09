def main():
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    data.sort()
    #print(data)
    count = 1
    for i in range(N-1):
        if data[i] == data[i+1]:
            continue
        else:
            count += 1
    print(count)
