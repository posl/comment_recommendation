def main():
    n,x = map(int,input().split())
    list1 = []
    for i in range(n):
        for j in range(65,91):
            list1.append(chr(j))
    print(list1[x-1])
