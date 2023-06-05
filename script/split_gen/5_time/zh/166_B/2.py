def main():
    n,k = map(int,input().split())
    d = []
    for i in range(k):
        d.append(int(input()))
        d.append(list(map(int,input().split())))
    #print(d)
    count = 0
    for i in range(1,n+1):
        flag = 0
        for j in range(1,len(d),2):
            if i in d[j]:
                flag = 1
                break
        if flag == 0:
            count += 1
    print(count)
