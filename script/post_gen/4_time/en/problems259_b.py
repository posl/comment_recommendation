Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, d = map(int, input().split())
    print(a * math.cos(math.radians(d)) - b * math.sin(math.radians(d)), a * math.sin(math.radians(d)) + b * math.cos(math.radians(d)))

=======
Suggestion 2

def rotate(a, b, d):
    import math
    theta = math.radians(d)
    x = a * math.cos(theta) - b * math.sin(theta)
    y = a * math.sin(theta) + b * math.cos(theta)
    return x, y

=======
Suggestion 3

def rotate(a, b, d):
    import math
    rad = math.radians(d)
    a_dash = a * math.cos(rad) - b * math.sin(rad)
    b_dash = a * math.sin(rad) + b * math.cos(rad)
    return a_dash, b_dash

=======
Suggestion 4

def rotate(x,y,deg):
    import math
    rad = math.radians(deg)
    x1 = x*math.cos(rad) - y*math.sin(rad)
    y1 = x*math.sin(rad) + y*math.cos(rad)
    return x1,y1

x,y,deg = map(int,input().split())
ans = rotate(x,y,deg)
print(ans[0],ans[1])

=======
Suggestion 5

def main():
    x, y, d = map(int, input().split())
    d = d * math.pi / 180
    print(x * math.cos(d) - y * math.sin(d), x * math.sin(d) + y * math.cos(d))

=======
Suggestion 6

def rotate_point(a, b, d):
    import math
    rad = math.radians(d)
    a_new = a*math.cos(rad)-b*math.sin(rad)
    b_new = a*math.sin(rad)+b*math.cos(rad)
    return a_new, b_new

=======
Suggestion 7

def main():
    import math
    a,b,d = map(int, input().split())
    d = math.radians(d)
    print(a*math.cos(d)-b*math.sin(d),a*math.sin(d)+b*math.cos(d))

=======
Suggestion 8

def main():
    a,b,d = map(int,input().split())
    import math
    d = math.radians(d)
    import numpy as np
    x = np.array([[math.cos(d),-math.sin(d)],[math.sin(d),math.cos(d)]])
    y = np.array([[a],[b]])
    ans = np.dot(x,y)
    print(ans[0][0],ans[1][0])

=======
Suggestion 9

def rotate(x,y,d):
    return x*math.cos(math.radians(d)) - y*math.sin(math.radians(d)), x*math.sin(math.radians(d)) + y*math.cos(math.radians(d))

import sys
import math

for line in sys.stdin:
    x,y,d = map(float,line.split())
    x,y = rotate(x,y,d)
    print(x,y)

=======
Suggestion 10

def rotate(a, b, d):
    # 2d matrix
    matrix = [[0 for i in range(2)] for j in range(2)]
    matrix[0][0] = math.cos(math.radians(d))
    matrix[0][1] = -1 * math.sin(math.radians(d))
    matrix[1][0] = math.sin(math.radians(d))
    matrix[1][1] = math.cos(math.radians(d))

    # 2d vector
    vector = [[0 for i in range(1)] for j in range(2)]
    vector[0][0] = a
    vector[1][0] = b

    # multiply matrix and vector
    result = [[0 for i in range(1)] for j in range(2)]
    for i in range(len(matrix)):
        for j in range(len(vector[0])):
            for k in range(len(vector)):
                result[i][j] += matrix[i][k] * vector[k][j]

    return result[0][0], result[1][0]
