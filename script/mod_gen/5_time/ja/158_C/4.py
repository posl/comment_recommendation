def calc_tax(n, tax):
    return int(n * tax)
A, B = map(int, input().split())
for i in range(1, 1000):
    if calc_tax(i, 0.08) == A and calc_tax(i, 0.1) == B:
        print(i)
        exit()
print(-1)

if __name__ == '__main__':
    calc_tax()