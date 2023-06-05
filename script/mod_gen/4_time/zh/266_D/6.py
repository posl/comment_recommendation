def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke.append((t, x, a))
    snuke.sort(key=lambda x: x[0])
    t = 0
    x = 0
    max_a = 0
    for i in range(n):
        if snuke[i][0] >= abs(snuke[i][1] - x) + t:
            max_a += snuke[i][2]
            t = snuke[i][0]
            x = snuke[i][1]
    print(max_a)

if __name__ == '__main__':
    main()