def round(x, k):
    for i in range(k):
        if x % 10 != 0:
            x = x + 10 - (x % 10)
        else:
            x = x // 10
    return x
x, k = map(int, input().split())
print(round(x, k))

if __name__ == '__main__':
    round()