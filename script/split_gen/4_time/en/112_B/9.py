def main():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    cost = 1001
    for i in c:
        if i[1] <= t:
            if cost > i[0]:
                cost = i[0]
    if cost == 1001:
        print("TLE")
    else:
        print(cost)
