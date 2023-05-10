def bonus_rooms(n,m,t,a,x,y):
  time_limit = t
  current_room = 1
  for i in range(n-1):
    time_limit -= a[i]
    if time_limit <= 0:
      return False
    if current_room in x:
      time_limit = min(t, time_limit + y[x.index(current_room)])
    current_room += 1
  return True
n,m,t = map(int, input().split())
a = list(map(int, input().split()))
x = []
y = []
for i in range(m):
  x_i, y_i = map(int, input().split())
  x.append(x_i)
  y.append(y_i)

if __name__ == '__main__':
    bonus_rooms()