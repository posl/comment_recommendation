Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if p[i] == i+1:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    max = 0
    for i in range(n):
        count = 0
        j = i
        while j != -1:
            j = p[j] - 1
            count += 1
        if max < count:
            max = count
    print(max)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    g = [0] * n
    for i in range(n):
        if p[i] == 0:
            continue
        g[i] = g[p[i]-1] + 1
    print(max(g))

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    max = 0
    for i in range(n):
        count = 0
        j = i
        while True:
            j = p[j] - 1
            count += 1
            if j == -1:
                break
        if max < count:
            max = count
    print(max)

main()

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        p = P[i]
        if p == 1:
            ans += 1
            break
        ans += 1

    print(ans)

=======
Suggestion 6

def get_input():
    N = int(input())
    P = list(map(int, input().split()))
    return N, P

=======
Suggestion 7

def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    max_generation = 0
    for i in range(n):
        generation = 1
        p = p_list[i]
        while (p != -1):
            generation += 1
            p = p_list[p - 1]
        if (generation > max_generation):
            max_generation = generation
    print(max_generation)

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))

    max_gen = 0
    for i in range(N):
        gen = 1
        parent = i+1
        while parent != -1:
            parent = P[parent-1]-1
            gen += 1
        max_gen = max(max_gen, gen)

    print(max_gen-1)

=======
Suggestion 9

def problem263_b():
    N = int(input())
    P = [int(x) for x in input().split()]

    max_gen = 0
    for i in range(N):
        gen = 0
        p = i + 1
        while p != -1:
            gen += 1
            p = P[p-1]
        if gen > max_gen:
            max_gen = gen

    print(max_gen)

=======
Suggestion 10

def getNumOfGeneration(N, P):
    result = 0
    for i in range(1, N):
        if P[i] == 1:
            if result < i:
                result = i
        else:
            result += 1
    return result
