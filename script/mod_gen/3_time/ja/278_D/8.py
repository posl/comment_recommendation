def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    query1 = [i for i in query if i[0] == 1]
    query2 = [i for i in query if i[0] == 2]
    query3 = [i for i in query if i[0] == 3]
    #print(query1)
    #print(query2)
    #print(query3)
    for i in query1:
        a = [i[1] for _ in range(n)]
    #print(a)
    for i in query2:
        a[i[1]-1] += i[2]
    #print(a)
    for i in query3:
        print(a[i[1]-1])
main()
