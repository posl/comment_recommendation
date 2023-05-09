def main():
    inputdata = []
    for i in range(4):
        a, b = map(int, input().split())
        inputdata.append([a, b])
    def cross(a, b):
        return a[0]*b[1] - a[1]*b[0]
    v = []
    for i in range(4):
        v.append([inputdata[(i+1)%4][0]-inputdata[i][0], inputdata[(i+1)%4][1]-inputdata[i][1]])
    s = [cross(v[0], v[1]), cross(v[1], v[2]), cross(v[2], v[3]), cross(v[3], v[0])]
    if s.count(0) == 0 and s.count(-0) == 0:
        if s.count(-1) == 0 and s.count(1) == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()