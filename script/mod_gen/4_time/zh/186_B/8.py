def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_num = min(map(min, A))
    print(sum(map(lambda x: sum(map(lambda y: y - min_num, x)), A)))

if __name__ == '__main__':
    main()