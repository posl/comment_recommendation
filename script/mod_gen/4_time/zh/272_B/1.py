def main():
    n,m = map(int,input().split())
    ans = "No"
    people = []
    for i in range(m):
        people.append(list(map(int,input().split())))
    for i in range(m):
        for j in range(i+1,m):
            if len(set(people[i][1:]).intersection(set(people[j][1:]))) > 0:
                ans = "Yes"
                break
    print(ans)
main()
