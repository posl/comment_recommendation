def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.sort()
    d_list = []
    for i in range(n-1):
        d_list.append(x_list[i+1]-x_list[i])
    #print(d_list)
    g = d_list[0]
    for i in range(1, len(d_list)):
        g = gcd(g, d_list[i])
    print(g)

if __name__ == '__main__':
    main()