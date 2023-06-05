def solve():
    n, m = [int(i) for i in input().split()]
    people = []
    for i in range(m):
        people.append([int(i) for i in input().split()][1:])
    for i in range(n):
        for j in range(i + 1, n):
            for k in people:
                if i + 1 in k and j + 1 in k:
                    break
            else:
                print("No")
                return
    print("Yes")
solve()
