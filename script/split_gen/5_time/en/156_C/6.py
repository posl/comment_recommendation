def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    min_stamina = 10000000
    for i in range(x[0], x[n-1]+1):
        stamina = 0
        for j in range(n):
            stamina += (x[j] - i) ** 2
        if stamina < min_stamina:
            min_stamina = stamina
    print(min_stamina)
