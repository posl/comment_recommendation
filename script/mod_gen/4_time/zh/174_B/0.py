def distance(x, y):
    return (x**2 + y**2)**0.5
N, D = map(int, input().split())
count = 0
for i in range(N):
    x, y = map(int, input().split())
    if distance(x, y) <= D:
        count += 1
print(count)

if __name__ == '__main__':
    distance()