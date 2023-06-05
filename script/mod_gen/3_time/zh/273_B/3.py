def round_up(n, d):
    return (n//d+1)*d
x, k = map(int, input().split())
ans = x
for i in range(k):
    ans = round_up(ans, 10**(i+1))
print(ans)

if __name__ == '__main__':
    round_up()