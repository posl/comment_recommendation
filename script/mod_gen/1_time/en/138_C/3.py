def main():
    N = int(input())
    V = list(map(int, input().split()))
    V.sort()
    while len(V) > 1:
        V.append((V.pop(0) + V.pop(0)) / 2)
    print(V[0])

if __name__ == '__main__':
    main()