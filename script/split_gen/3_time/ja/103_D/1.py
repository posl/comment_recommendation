def main():
    n,m = map(int,input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    a.sort()
    b.sort()
    #print(a)
    #print(b)
    a_max = a[m-1]
    b_min = b[0]
    #print(a_max)
    #print(b_min)
    if a_max < b_min:
        print(b_min - a_max)
    else:
        print(0)
