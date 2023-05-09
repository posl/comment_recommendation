def main():
    n = int(input())
    x_list = []
    y_list = []
    for i in range(n):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
    #print(x_list)
    #print(y_list)
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += ((x_list[i]-x_list[j])**2+(y_list[i]-y_list[j])**2)**(1/2)
            #print(sum)
    print(sum/(math.factorial(n)))

if __name__ == '__main__':
    main()