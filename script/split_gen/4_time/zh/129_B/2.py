def main():
    n = int(input())
    ws = [int(x) for x in input().split()]
    min = 100000
    for i in range(1, n):
        s1 = sum(ws[:i])
        s2 = sum(ws[i:])
        if abs(s1 - s2) < min:
            min = abs(s1 - s2)
    print(min)
main()
