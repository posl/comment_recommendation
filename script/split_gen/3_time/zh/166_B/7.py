def main():
    n,k = map(int,input().split())
    list1 = []
    for i in range(k):
        d = int(input())
        list1.append(list(map(int,input().split())))
    list2 = []
    for i in range(n):
        list2.append(0)
    for i in range(k):
        for j in range(len(list1[i])):
            list2[list1[i][j]-1] += 1
    print(list2.count(0))
