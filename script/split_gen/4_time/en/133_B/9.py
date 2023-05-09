def is_integer_distance(x, y):
  distance = 0
  for i in range(len(x)):
    distance += (x[i] - y[i]) ** 2
  if distance ** (1/2) % 1 == 0:
    return True
  else:
    return False
n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
count = 0
for i in range(n):
  for j in range(i+1, n):
    if is_integer_distance(x[i], x[j]):
      count += 1
print(count)
