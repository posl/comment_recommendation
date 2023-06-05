def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort(reverse=True)
    price = sum(p)
    price -= p[0] / 2
    print(int(price))
