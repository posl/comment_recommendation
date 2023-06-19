def main():
    h,w = map(int,input().split())
    l = []
    for i in range(h):
        l.append(list(input()))
    for i in range(w):
        x = 0
        for j in range(h):
            if l[j][i] == "#":
                x += 1
        print(x,end=" ")
