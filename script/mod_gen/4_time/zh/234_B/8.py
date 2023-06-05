def main():
    import math
    N = int(input())
    list_x = []
    list_y = []
    for i in range(N):
        x,y = map(int,input().split())
        list_x.append(x)
        list_y.append(y)
    max_length = 0
    for i in range(N):
        for j in range(i+1,N):
            length = math.sqrt((list_x[i]-list_x[j])**2 + (list_y[i]-list_y[j])**2)
            if length > max_length:
                max_length = length
    print(max_length)

if __name__ == '__main__':
    main()