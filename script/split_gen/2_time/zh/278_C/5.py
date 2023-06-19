def main():
    n,q = input().split(" ")
    n = int(n)
    q = int(q)
    t = []
    a = []
    b = []
    for i in range(q):
        t_i,a_i,b_i = input().split(" ")
        t.append(int(t_i))
        a.append(int(a_i))
        b.append(int(b_i))
    #print(t)
    #print(a)
    #print(b)
    #print(n)
    #print(q)
    follow = []
    for i in range(n):
        follow.append([])
    for i in range(q):
        if t[i] == 1:
            follow[a[i]-1].append(b[i]-1)
        elif t[i] == 2:
            follow[a[i]-1].remove(b[i]-1)
        elif t[i] == 3:
            if a[i]-1 in follow[b[i]-1] and b[i]-1 in follow[a[i]-1]:
                print("Yes")
            else:
                print("No")
    #print(follow)
