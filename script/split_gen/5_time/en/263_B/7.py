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
