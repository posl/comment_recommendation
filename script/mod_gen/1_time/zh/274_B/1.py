def problems274_b():
    H,W = map(int,input().split())
    list = []
    for i in range(H):
        list.append(input())
    for i in range(W):
        count = 0
        for j in range(H):
            if list[j][i] == '#':
                count += 1
        print(count,end=' ')
    return

if __name__ == '__main__':
    problems274_b()