def main():
    N = int(input())
    h = list(map(int,input().split()))
    #print(N,h)
    #N = 4
    #h = [1,2,2,1]
    #N = 5
    #h = [3,1,2,3,1]
    #N = 8
    #h = [4,23,75,0,23,96,50,100]
    #N = 100
    #h = [0] * N
    #print(N,h)
    count = 0
    for i in range(N):
        if h[i] > h[i-1]:
            count += h[i] - h[i-1]
    print(count)
    return count
