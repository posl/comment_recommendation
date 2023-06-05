def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        temp = input().split()
        edges.append([int(temp[0]),int(temp[1]),int(temp[2])])
    edges.sort(key=lambda x:x[2])
    edges.reverse()
    sum = 0
    for i in range(n-1):
        sum += edges[i][2]*(i+1)*(n-i-1)
    print(sum)
