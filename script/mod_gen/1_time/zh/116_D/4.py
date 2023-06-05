def main():
    n, k = map(int, input().split())
    t_d = []
    for i in range(n):
        t_d.append(list(map(int, input().split())))
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_d.sort(key=lambda x: x[1], reverse=True)
    t_d.sort(key=lambda x: x[0])
    t_set = set()
    d_sum = 0
    for i in range(k):
        d_sum += t_d[i][1]
        t_set.add(t_d[i][0])
    t_set_length = len(t_set)
    d_sum += t_set_length ** 2
    print(d_sum)

if __name__ == '__main__':
    main()