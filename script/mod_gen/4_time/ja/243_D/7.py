def move(s, x):
    if s == 'U':
        return x // 2
    elif s == 'L':
        return x * 2
    else:
        return x * 2 + 1
n, x = map(int, input().split())
s = input()
for i in range(n):
    x = move(s[i], x)
print(x)

if __name__ == '__main__':
    move()