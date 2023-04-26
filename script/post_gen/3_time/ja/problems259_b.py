Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,d = map(int, input().split())
    theta = math.radians(d)
    x = a * math.cos(theta) - b * math.sin(theta)
    y = a * math.sin(theta) + b * math.cos(theta)
    print(x,y)

=======
Suggestion 2

def main():
    a,b,d = map(int,input().split())
    import math
    rad = math.radians(d)
    x = a*math.cos(rad) - b*math.sin(rad)
    y = a*math.sin(rad) + b*math.cos(rad)
    print(x,y)

=======
Suggestion 3

def main():
    a,b,d = map(int, input().split())
    import math
    rad = math.radians(d)
    x = a*math.cos(rad) - b*math.sin(rad)
    y = a*math.sin(rad) + b*math.cos(rad)
    print(x,y)
main()

=======
Suggestion 4

def main():
    a,b,d = map(int,input().split())
    import math
    rad = math.radians(d)
    x = math.cos(rad)*a - math.sin(rad)*b
    y = math.sin(rad)*a + math.cos(rad)*b
    print(x,y)

=======
Suggestion 5

def main():
    a,b,d = map(int,input().split())
    rad = d * 3.141592653589793 / 180
    x = a * math.cos(rad) - b * math.sin(rad)
    y = a * math.sin(rad) + b * math.cos(rad)
    print(x,y)

=======
Suggestion 6

def main():
    a, b, d = map(int, input().split())
    rad = d * (math.pi/180)
    x = a * math.cos(rad) - b * math.sin(rad)
    y = a * math.sin(rad) + b * math.cos(rad)
    print(x, y)

=======
Suggestion 7

def main():
    a,b,d = map(int, input().split())
    from math import sin, cos, pi
    rad = d * pi / 180
    x = a * cos(rad) - b * sin(rad)
    y = a * sin(rad) + b * cos(rad)
    print(x,y)

main()

=======
Suggestion 8

def main():
    a, b, d = map(int, input().split())
    import math
    rad = math.radians(d)
    import numpy as np
    x = np.array([a, b])
    rotate_matrix = np.array([[math.cos(rad), -math.sin(rad)], [math.sin(rad), math.cos(rad)]])
    y = np.dot(rotate_matrix, x)
    print(y[0], y[1])

=======
Suggestion 9

def main():
    # 標準入力から値を取得してinput_lineに入れる
    input_line = input()
    #print(input_line)
    #input_line = "2 2 180"
    #input_line = "5 0 120"
    #input_line = "0 0 11"
    #inp
