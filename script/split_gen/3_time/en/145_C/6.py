def main():
    N = int(input())
    town = []
    for i in range(N):
        x, y = map(int, input().split())
        town.append((x, y))
    from itertools import permutations
    perm = permutations(range(N))
    ans = 0
    for p in perm:
        for i in range(N-1):
            ans += ((town[p[i]][0]-town[p[i+1]][0])**2+(town[p[i]][1]-town[p[i+1]][1])**2)**(1/2)
    print(ans/N/math.factorial(N))
