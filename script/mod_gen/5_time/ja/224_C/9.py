def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N=int(input())
    points=[]
    for i in range(N):
        x,y=map(int,input().split())
        points.append((x,y))
    #print(points)
    #print(N)
    #print(points[0][0])
    #print(points[0][1])
    #print(points[0][0]*points[1][1]-points[1][0]*points[0][1])
    #print(points[1][0]*points[2][1]-points[2][0]*points[1][1])
    #print(points[2][0]*points[0][1]-points[0][0]*points[2][1])
    #print((points[0][0]*points[1][1]-points[1][0]*points[0][1])+(points[1][0]*points[2][1]-points[2][0]*points[1][1])+(points[2][0]*points[0][1]-points[0][0]*points[2][1]))
    #print((points[0][0]*points[1][1]-points[1][0]*points[0][1])+(points[1][0]*points[2][1]-points[2][0]*points[1][1])+(points[2][0]*points[0][1]-points[0][0]*points[2][1]))
    #print((points[0][0]*points[1][1]-points[1][0]*points[0][1])+(points[1][0]*points[2][1]-points[2][0]*points[1][1])+(points[2][0]*points[0][1]-points[0][0]*points[2][1]))
    #print((points[0][0]*points[1][1]-points[1][0]*points[0][1])+(points[1][0]*points[2][1]-points[2][0]*points[1][1])+(points[2][0]*points[0][1]-points[0][0]*points[2][1]))
    #print((points[0][0]*points[1][1]-points[1][0]*points[0][1])

if __name__ == '__main__':
    main()