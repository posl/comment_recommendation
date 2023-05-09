def calc_distance(x,y):
    return (x**2+y**2)**(1/2)
n,d = map(int,input().split())
count = 0
for i in range(n):
    x,y = map(int,input().split())
    if calc_distance(x,y) <= d:
        count += 1
print(count)

if __name__ == '__main__':
    calc_distance()