def round_up(x, y):
    if x % y == 0:
        return x
    else:
        return x + y - x % y
x, k = map(int, input().split())
for i in range(k):
    x = round_up(x, 10**(k-i))
print(x)

if __name__ == '__main__':
    round_up()