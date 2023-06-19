def get_distance(x, y):
    return pow(pow(x, 2) + pow(y, 2), 0.5)
n, d = map(int, input().split())
count = 0
for i in range(n):
    x, y = map(int, input().split())
    if get_distance(x, y) <= d:
        count += 1
print(count)

if __name__ == '__main__':
    get_distance()