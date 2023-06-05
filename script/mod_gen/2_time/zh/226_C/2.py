def main():
    N = int(input())
    l = []
    for i in range(N):
        l.append(list(map(int, input().split()))[1:])
    print(len(set([tuple(i) for i in l])))

if __name__ == '__main__':
    main()