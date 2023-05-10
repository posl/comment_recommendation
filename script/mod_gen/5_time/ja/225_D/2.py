def main():
    N, Q = map(int, input().split())
    trains = [[i, i] for i in range(N)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            if trains[query[1]-1][1] == trains[query[2]-1][0]:
                continue
            else:
                trains[trains[query[1]-1][1]-1][0] = trains[query[2]-1][0]
                trains[query[2]-1][0] = trains[query[1]-1][0]
                trains[query[1]-1][1] = trains[query[2]-1][1]
                trains[query[2]-1][1] = trains[trains[query[1]-1][1]-1][1]
        elif query[0] == 2:
            if trains[query[1]-1][1] == trains[query[2]-1][0]:
                trains[query[1]-1][1] = trains[query[2]-1][1]
                trains[trains[query[2]-1][1]-1][0] = trains[query[1]-1][1]
                trains[query[2]-1][1] = trains[query[1]-1][0]
                trains[trains[query[1]-1][0]-1][1] = trains[query[2]-1][1]
            else:
                continue
        elif query[0] == 3:
            output = []
            index = query[1]-1
            while True:
                output.append(index+1)
                if index == trains[index][1]-1:
                    break
                else:
                    index = trains[index][1]-1
            print(len(output), *output)
        else:
            continue

if __name__ == '__main__':
    main()