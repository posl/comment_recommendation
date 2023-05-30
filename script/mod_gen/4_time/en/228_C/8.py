def rank(N, K, P):
    students = []
    for i in range(N):
        students.append(sum(P[i]))
    students.sort(reverse=True)
    if students[K-1] == students[K]:
        return 'No'
    else:
        return 'Yes'
N, K = map(int, input().split())
P = [list(map(int, input().split())) for i in range(N)]
print(rank(N, K, P))
