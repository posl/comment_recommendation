def main():
    n, m = map(int, input().split())
    people = [[] for i in range(n)]
    for i in range(m):
        k, *x = map(int, input().split())
        for j in x:
            people[j-1].append(i)
    for i in range(n):
        people[i] = set(people[i])
    for i in range(n):
        for j in range(i+1, n):
            if people[i] & people[j] == set():
                print('No')
                return
    print('Yes')
