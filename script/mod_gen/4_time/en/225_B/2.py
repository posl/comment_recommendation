def main():
    n = int(input())
    c = [0] * n
    for i in range(n-1):
        a,b = map(int, input().split())
        c[a-1] += 1
        c[b-1] += 1
    if c.count(1) == 1 and c.count(n-1) == 1:
        print("Yes")
    else:
        print("No")
main()
