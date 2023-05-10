def main():
    #input
    n,k = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #compute
    village = 0
    money = k
    for i in range(n):
        if a[i] > village:
            break
        else:
            money += b[i]
            village = a[i]
    village += money
    #output
    print(village)
