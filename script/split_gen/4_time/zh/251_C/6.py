def main():
    n = int(input())
    st = {}
    for i in range(n):
        s,t = input().split()
        t = int(t)
        if s in st:
            if st[s][0] < t:
                st[s] = [t,i]
        else:
            st[s] = [t,i]
    #print(st)
    max = 0
    for k in st:
        if st[k][0] > max:
            max = st[k][0]
            max_i = st[k][1]
    print(max_i+1)
