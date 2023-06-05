def main():
    n,s,d = input().split()
    n,s,d = int(n),int(s),int(d)
    lst = []
    for i in range(n):
        x,y = input().split()
        x,y = int(x),int(y)
        lst.append([x,y])
    for item in lst:
        if item[0] < s and item[1] > d:
            print("Yes")
            return
    print("No")
    return
