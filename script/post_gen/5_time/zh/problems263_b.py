Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def get_generation(n, p):
    if n == 1:
        return 0
    else:
        return get_generation(p[n-1], p) + 1

n = int(input())
p = list(map(int, input().split()))
print(get_generation(n, p))

=======
Suggestion 3

def getGen(n, p):
    gen = 1
    while p != 1:
        gen += 1
        p = n[p-2]
    return gen

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        x = i + 1
        while x != -1:
            x = P[x - 1]
            ans += 1
            if x == 0:
                break
    print(ans)

=======
Suggestion 5

def get_generation_count(persons, person_id):
    if person_id == 1:
        return 0
    else:
        return get_generation_count(persons, persons[person_id - 1]) + 1

=======
Suggestion 6

def generation(N, p):
    generation = 0
    for i in range(N):
        generation += 1
        if p[i] == 1:
            break
        generation += generation(p[i]-1, p)
    return generation

=======
Suggestion 7

def count_generation(n, parent):
    count = 0
    for i in range(n):
        p = parent[i]
        while p != -1:
            count += 1
            p = parent[p-1]
    return count

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(1, N+1):
        x = i
        while x != -1:
            x = P[x-1]
            ans += 1
    print(ans)

=======
Suggestion 9

def getGeneration(n, p):
    generation = 1
    for i in range(1, n):
        if p[i] == 1:
            generation += 1
        else:
            generation = getGeneration(p[i], p) + 1
    return generation

=======
Suggestion 10

def get_generation(n, p):
    if n == 1:
        return 0
    else:
        return get_generation(p[n-1], p) + 1
