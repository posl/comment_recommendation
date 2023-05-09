def main():
    N = int(input())
    lst = []
    for i in range(N):
        S, P = input().split()
        lst.append([S, int(P), i+1])
    lst.sort(key=lambda x: (-x[1], x[0], x[2]))
    for i in range(N):
        print(lst[i][2])

if __name__ == '__main__':
    main()