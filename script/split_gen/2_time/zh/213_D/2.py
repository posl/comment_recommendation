def main():
    h,w,n = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_,b_ = map(int,input().split())
        a.append(a_)
        b.append(b_)
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    a_index = {}
    b_index = {}
    for i in range(len(a)):
        a_index[a[i]] = i+1
    for i in range(len(b)):
        b_index[b[i]] = i+1
    for i in range(n):
        print(a_index[a[i]],b_index[b[i]])
