def get_num():
    N = input()
    a = raw_input()
    a = a.split(' ')
    a = map(int, a)
    a.sort()
    a.append(0)
    count = 1
    for i in range(1, N):
        if a[i] != a[i - 1]:
            count += 1
    print count

if __name__ == '__main__':
    get_num()