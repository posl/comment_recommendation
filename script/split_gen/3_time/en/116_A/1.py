def area_of_triangle(a,b,c):
    s = (a + b + c)/2
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5
a, b, c = [int(x) for x in input().split()]
print(int(area_of_triangle(a,b,c)))
