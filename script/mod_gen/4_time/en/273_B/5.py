def round_up(num, unit):
    if num % unit == 0:
        return num
    else:
        return (num // unit + 1) * unit
x, k = map(int, input().split())
for i in range(k):
    x = round_up(x, 10 ** (k - i))
print(x)

if __name__ == '__main__':
    round_up()