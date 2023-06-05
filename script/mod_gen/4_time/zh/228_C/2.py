def main():
    n,k = map(int, input().split())
    n_list = []
    for i in range(n):
        n_list.append(list(map(int, input().split())))
    print(n_list)
    print(n,k)

if __name__ == '__main__':
    main()