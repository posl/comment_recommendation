def main():
    N = int(input())
    ladders = []
    for i in range(N):
        A, B = map(int, input().split())
        ladders.append((A, B))
    ladders.sort(key=lambda x: x[1])
    current_floor = 1
    for i in range(N):
        if ladders[i][0] >= current_floor:
            current_floor = ladders[i][1]
    print(current_floor)

if __name__ == '__main__':
    main()