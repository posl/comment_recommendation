def main():
 N, Q = map(int, input().split())
 
 #parent[x] は、xの親の番号を格納する。親がいない場合は-(その集合のサイズ)
 #初期状態では、全てが根であるため、-1を代入する。
 parent = [-1] * N
 
 for _ in range(Q):
  c, x, y = map(int, input().split())
  x -= 1
  y -= 1
 
  if c == 1:
   unite(parent, x, y)
 
  elif c == 2:
   root_x = find_root(parent, x)
   root_y = find_root(parent, y)
   if root_x == root_y:
    parent[root_x] += 1
    parent[root_y] = x
 
  else:
   root_x = find_root(parent, x)
   root_y = find_root(parent, y)
   if root_x == root_y:
    print(size(parent, x))
    print(*sorted(connected_cars(parent, x)))
   else:
    print(0)
