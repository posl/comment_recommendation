def main():
    n,m = map(int,input().split())
    if n == 2 and m == 0:
        print("No")
        return
    if m == 0:
        print("Yes")
        return
    data = []
    for i in range(m):
        data.append(list(map(int,input().split())))
    data = sorted(data,key = lambda x:x[0])
    for i in range(len(data)-1):
        if data[i][0] == data[i+1][0]:
            print("No")
            return
    data = sorted(data,key = lambda x:x[1])
    for i in range(len(data)-1):
        if data[i][1] == data[i+1][1]:
            print("No")
            return
    print("Yes")
    return
