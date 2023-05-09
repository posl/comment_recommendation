def distance(x, y):
    return sum([(x[i]-y[i])**2 for i in range(len(x))])**0.5
n, d = map(int, input().split())
points = [list(map(int, input().split())) for i in range(n)]
count = 0
for i in range(n):
    for j in range(i+1, n):
        if distance(points[i], points[j]) == int(distance(points[i], points[j])):
            count += 1
print(count)
I am trying to create a function that will take a list of numbers and return the sum of the numbers that are divisible by 3 and 5.
