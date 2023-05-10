def main():
    n, q = map(int, input().split())
    cars = [i for i in range(n)]
    front = [i for i in range(n)]
    back = [i for i in range(n)]
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            front[back[cars[query[2]-1]]] = front[cars[query[1]-1]]
            back[front[cars[query[1]-1]]] = back[cars[query[2]-1]]
            front[cars[query[1]-1]] = cars[query[2]-1]
            back[cars[query[2]-1]] = cars[query[1]-1]
            cars[query[2]-1] = cars[query[1]-1]
        elif query[0] == 2:
            front[back[cars[query[2]-1]]] = cars[query[1]-1]
            back[front[cars[query[1]-1]]] = cars[query[2]-1]
            cars[query[1]-1] = front[cars[query[1]-1]]
            cars[query[2]-1] = back[cars[query[2]-1]]
            front[cars[query[1]-1]] = query[1]-1
            back[cars[query[2]-1]] = query[2]-1
        else:
            ans = []
            car = cars[query[1]-1]
            while car != n:
                ans.append(car+1)
                car = front[car]
            print(len(ans), *ans)
    return

if __name__ == '__main__':
    main()