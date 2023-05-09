def main():
    # Read input
    N = int(input())
    p = []
    for _ in range(N):
        p.append(int(input()))
    # Find the highest value
    max_value = max(p)
    # Find the total amount
    total = 0
    for i in range(N):
        if p[i] == max_value:
            total += p[i] / 2
        else:
            total += p[i]
    # Print the total amount
    print(int(total))

if __name__ == '__main__':
    main()