def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    print('Yes' if len(set(map(tuple, name))) != N else 'No')

if __name__ == '__main__':
    main()