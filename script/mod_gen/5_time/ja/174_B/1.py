def get_distance(x,y):
    return (x**2 + y**2)**(1/2)
N,D = map(int, input().split())
count = 0
for i in range(N):
    x,y = map(int, input().split())
    distance = get_distance(x,y)
    if distance <= D:
        count += 1
print(count)

if __name__ == '__main__':
    get_distance()