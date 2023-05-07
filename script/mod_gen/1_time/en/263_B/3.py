def main():
    n = int(input())
    parent = [int(x) for x in input().split()]
    generation = 0
    while n != 1:
        n = parent[n-2]
        generation += 1
    print(generation)

if __name__ == '__main__':
    main()