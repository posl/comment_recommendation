def main():
    N, Q = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    train = [i for i in range(N)]
    for q in query:
        if q[0] == 1:
            train[q[2]-1], train[q[1]-1] = train[q[1]-1], train[q[2]-1]
        elif q[0] == 2:
            train[q[1]-1], train[q[2]-1] = train[q[2]-1], train[q[1]-1]
        else:
            tmp = []
            for i in range(N):
                if train[i] == train[q[1]-1]:
                    tmp.append(i+1)
            ans.append(tmp)
    for a in ans:
        print(len(a), *a)
