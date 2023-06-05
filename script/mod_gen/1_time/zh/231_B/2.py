def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    d = {}
    for name in S:
        if name in d:
            d[name] += 1
        else:
            d[name] = 1
    max = 0
    max_name = ''
    for name in d:
        if d[name] > max:
            max = d[name]
            max_name = name
    print(max_name)

if __name__ == '__main__':
    main()