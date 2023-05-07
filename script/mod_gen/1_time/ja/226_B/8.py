def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(tuple(map(int, input().split())))
    
    print(len(set(L)))

if __name__ == '__main__':
    main()