def move(x):
    if x == '1':
        return '0'
    else:
        return '1'
s = input()
ans = ''
for i in s:
    ans += move(i)
print(ans)

if __name__ == '__main__':
    move()