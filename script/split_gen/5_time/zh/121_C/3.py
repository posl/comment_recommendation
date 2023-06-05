def main():
    n,m = map(int,input().split())
    a_b = []
    for i in range(n):
        a_b.append(list(map(int,input().split())))
    a_b.sort(key=lambda x:x[0])
    #print(a_b)
    count = 0
    money = 0
    for i in range(n):
        if count >= m:
            break
        if count + a_b[i][1] <= m:
            count += a_b[i][1]
            money += a_b[i][0] * a_b[i][1]
        else:
            money += (m - count) * a_b[i][0]
            count += (m - count)
    print(money)
