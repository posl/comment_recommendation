def main():
    N = int(input())
    R = []
    for i in range(N):
        L, R = map(int, input().split())
        R.append((L, R))
    R.sort(key=lambda x: x[0])
    r = []
    for i in range(N):
        if r == []:
            r.append(R[i])
        else:
            if r[-1][1] < R[i][0]:
                r.append(R[i])
            else:
                r[-1] = (r[-1][0], max(r[-1][1], R[i][1]))
    for i in range(len(r)):
        print(r[i][0], r[i][1])
