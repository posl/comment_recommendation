def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    q = int(input())
    query = [input().split() for _ in range(q)]
    #print(query)
    #print(a)
    for i in query:
        if i[0] == '1':
            a = [int(i[1]) for _ in range(n)]
        elif i[0] == '2':
            a[int(i[1])-1] += int(i[2])
        else:
            print(a[int(i[1])-1])
