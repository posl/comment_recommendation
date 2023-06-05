def get_honest_person_count(N, A, xy):
    honest_person_count = 0
    for i in range(2**N):
        honest_person = []
        for j in range(N):
            if ((i >> j) & 1):
                honest_person.append(j + 1)
        if len(honest_person) <= honest_person_count:
            continue
        for k in range(len(honest_person)):
            for l in range(A[honest_person[k] - 1]):
                if xy[honest_person[k] - 1][l][1] == 0 and xy[honest_person[k] - 1][l][0] in honest_person:
                    break
            else:
                if k == len(honest_person) - 1:
                    honest_person_count = len(honest_person)
                    break
                else:
                    continue
            break
    return honest_person_count
N = int(input())
A = []
xy = []
for i in range(N):
    A.append(int(input()))
    xy.append([])
    for j in range(A[i]):
        xy[i].append(list(map(int, input().split())))
print(get_honest_person_count(N, A, xy))
