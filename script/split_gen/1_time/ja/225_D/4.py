def main():
    N, Q = [int(i) for i in input().split()]
    trains = [i for i in range(N)]
    for _ in range(Q):
        q = [int(i) for i in input().split()]
        if q[0] == 1:
            trains[q[1]-1] = q[2]-1
        elif q[0] == 2:
            trains[q[1]-1] = q[1]-1
        else:
            train = trains[q[1]-1]
            ans = [q[1]]
            while train != q[1]-1:
                ans.append(train+1)
                train = trains[train]
            print(len(ans),*ans)
