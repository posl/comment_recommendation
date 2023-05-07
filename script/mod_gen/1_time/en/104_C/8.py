def main():
    D, G = map(int, input().split())
    PC = []
    for i in range(D):
        p, c = map(int, input().split())
        PC.append((p, c))
    print(solve(D, G, PC))

if __name__ == '__main__':
    main()