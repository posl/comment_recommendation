def main():
    import sys
    N = int(sys.stdin.readline())
    towns = []
    for i in range(N):
        line = sys.stdin.readline().strip()
        towns.append(list(map(int, line.split())))
    import itertools
    import math
    total = 0
    for i in itertools.permutations(range(N)):
        for j in range(N-1):
            total += math.sqrt((towns[i[j]][0]-towns[i[j+1]][0])**2 + (towns[i[j]][1]-towns[i[j+1]][1])**2)
    print(total/math.factorial(N))

if __name__ == '__main__':
    main()