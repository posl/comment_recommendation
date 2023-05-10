def main():
    n = int(input())
    s = []
    p = []
    for i in range(n):
        s_i, p_i = input().split()
        s.append(s_i)
        p.append(int(p_i))
    restaurant = []
    for i in range(n):
        restaurant.append([s[i], p[i], i+1])
    restaurant.sort(key=lambda x: x[1], reverse=True)
    restaurant.sort(key=lambda x: x[0])
    for i in range(n):
        print(restaurant[i][2])

if __name__ == '__main__':
    main()