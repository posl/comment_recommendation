def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    #print(a)
    people = []
    for i in range(n):
        people.append(i+1)
    #print(people)
    for i in range(m):
        for j in range(a[i][0]):
            if a[i][j+1] in people:
                people.remove(a[i][j+1])
    #print(people)
    if len(people) == 0:
        print('Yes')
    else:
        print('No')
