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

if __name__ == '__main__':
    main()