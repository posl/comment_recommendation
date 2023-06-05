def search(a, b):
    if (a, b) in black:
        black.remove((a, b))
        search(a-1, b-1)
        search(a-1, b)
        search(a, b-1)
        search(a, b+1)
        search(a+1, b)
        search(a+1, b+1)
N = int(input())
black = set()
for i in range(N):
    a, b = map(int, input().split())
    black.add((a, b))
ans = 0
while len(black) > 0:
    a, b = black.pop()
    search(a, b)
    ans += 1
print(ans)
