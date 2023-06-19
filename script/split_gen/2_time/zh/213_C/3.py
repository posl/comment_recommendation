def main():
    h,w,n = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    a = sorted(set(a))
    b = sorted(set(b))
    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        a_dict[a[i]] = i+1
    for i in range(len(b)):
        b_dict[b[i]] = i+1
    for i in range(n):
        print(a_dict[a[i]],b_dict[b[i]])
