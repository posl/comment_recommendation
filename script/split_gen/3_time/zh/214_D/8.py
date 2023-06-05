def main():
    n = int(input())
    uvw = []
    for i in range(n-1):
        uvw.append(list(map(int,input().split())))
    print(uvw)
    for i in range(n-1):
        print(i)
        print(uvw[i][0],uvw[i][1])
        print(uvw[i][2])
