def main():
    nmq = input().split(" ")
    n = int(nmq[0])
    m = int(nmq[1])
    q = int(nmq[2])
    lr = []
    pq = []
    for i in range(m):
        lr.append(input().split(" "))
    for i in range(q):
        pq.append(input().split(" "))
    for i in range(q):
        count = 0
        for j in range(m):
            if int(pq[i][0]) <= int(lr[j][0]) and int(lr[j][1]) <= int(pq[i][1]):
                count += 1
        print(count)
