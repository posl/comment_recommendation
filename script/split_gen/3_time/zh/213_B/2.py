def main():
    n = int(input())
    a = list(map(int, input().split()))
    m1 = min(a)
    m2 = min([x for x in a if x != m1])
    print(a.index(m2) + 1)
main()
