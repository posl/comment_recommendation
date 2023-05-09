def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append([int(x) for x in input().split()])
    L.sort()
    L.append([0,0])
    count = 1
    for i in range(N):
        if L[i] != L[i+1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()