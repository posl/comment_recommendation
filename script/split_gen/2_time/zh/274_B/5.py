def problems274_b():
    h,w = map(int,input().split())
    box = []
    for i in range(h):
        box.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if box[j][i] == "#":
                count += 1
        print(count,end=" ")
    print()
