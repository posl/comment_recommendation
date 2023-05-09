def main():
    n = int(input())
    p = list(map(int, input().split()))
    max_gen = 0
    for i in range(n):
        gen = 0
        j = i
        while p[j] != -1:
            gen += 1
            j = p[j] - 1
        if gen > max_gen:
            max_gen = gen
    print(max_gen + 1)
