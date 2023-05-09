def main():
    s = input()
    q = int(input())
    t = [0] * q
    k = [0] * q
    for i in range(q):
        t[i], k[i] = map(int, input().split())
    s = s.replace('A', '1').replace('B', '2').replace('C', '3')
    s = s.replace('1', 'A').replace('2', 'B').replace('3', 'C')
    for i in range(q):
        print(s[(t[i] + k[i] - 1) % len(s)])

if __name__ == '__main__':
    main()