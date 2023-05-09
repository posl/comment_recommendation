def main():
    n = int(input())
    a_b = []
    for i in range(n):
        a_b.append(list(map(int, input().split())))
    total_a = 0
    total_b = 0
    for i in range(n):
        total_a += a_b[i][0] / a_b[i][1]
        total_b += 1 / a_b[i][1]
    print(total_a / total_b)

if __name__ == '__main__':
    main()