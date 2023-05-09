def main():
    N = int(input())
    stairs = []
    for i in range(N):
        A, B = map(int, input().split())
        stairs.append([A, B])
    stairs.sort(key=lambda x: x[1])
    #print(stairs)
    max = 0
    for i in range(N):
        if stairs[i][0] > max:
            max = stairs[i][0]
    print(max)

if __name__ == '__main__':
    main()