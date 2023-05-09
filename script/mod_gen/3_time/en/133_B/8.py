def get_distance(x,y):
    square_sum = 0
    for i in range(len(x)):
        square_sum += (x[i] - y[i])**2
    return int(square_sum**0.5)
n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(i+1,n):
        if get_distance(x[i], x[j])**2 == get_distance(x[i], x[j]):
            count += 1
print(count)

if __name__ == '__main__':
    get_distance()