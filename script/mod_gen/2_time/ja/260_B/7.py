def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_b = []
    for i in range(n):
        a_b.append([a[i], b[i], i + 1])
    a_b.sort(key=lambda x: x[0], reverse=True)
    a_b = a_b[:x]
    a_b.sort(key=lambda x: x[1], reverse=True)
    a_b = a_b[:y]
    a_b.sort(key=lambda x: x[0] + x[1], reverse=True)
    a_b = a_b[:z]
    a_b.sort(key=lambda x: x[2])
    for i in a_b:
        print(i[2])

if __name__ == '__main__':
    main()