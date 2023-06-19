def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1
    print(" ".join([str(x) for x in q]))

if __name__ == '__main__':
    main()