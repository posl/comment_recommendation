def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    #print(N)
    d = dict()
    for i in range(N-1):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
        if b[i] in d:
            d[b[i]] += 1
        else:
            d[b[i]] = 1
    #print(d)
    count = 0
    for k,v in d.items():
        if v == N-1:
            count += 1
    if count == 1:
        print("Yes")
    else:
        print("No")
