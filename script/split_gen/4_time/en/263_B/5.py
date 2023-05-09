def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    max_gen = 0
    for i in range(N):
        gen = 1
        while P[i] != 1:
            gen += 1
            i = P[i] - 1
        if gen > max_gen:
            max_gen = gen
    print(max_gen)
