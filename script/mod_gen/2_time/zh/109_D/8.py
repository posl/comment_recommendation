def main():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.sort()
    if n == 1:
        print(abs(x_list[0]-x))
    else:
        x_list.append(x)
        x_list.sort()
        x_list2 = []
        for i in range(n+1):
            x_list2.append(abs(x_list[i+1]-x_list[i]))
        print(gcd_list(x_list2))

if __name__ == '__main__':
    main()