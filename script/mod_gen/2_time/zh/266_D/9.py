def main():
    n = int(input())
    snuke = [0 for i in range(5)]
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke[x] = max(snuke[x], a)
    print(sum(snuke[1:]))
main()
