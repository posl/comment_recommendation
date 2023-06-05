def main():
    n,m,q = map(int,input().split())
    trains = []
    for i in range(m):
        trains.append(list(map(int,input().split())))
    for i in range(q):
        p,q = map(int,input().split())
        count = 0
        for j in range(m):
            if trains[j][0] >= p and trains[j][1] <= q:
                count += 1
        print(count)
