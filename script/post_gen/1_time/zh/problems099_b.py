Synthesizing 9/10 solutions

=======
Suggestion 1

def solve(a, b):
    # a是西边的塔，b是东边的塔
    # a = 1 + 2 + 3 + ... + x
    # b = 1 + 2 + 3 + ... + x + x + 1
    # a = x * (x + 1) / 2
    # b = (x + 1) * (x + 2) / 2
    # a * 2 = x * (x + 1)
    # b * 2 = (x + 1) * (x + 2)

=======
Suggestion 2

def snow(a,b):
    x = b - a
    y = x*(x+1)/2
    return int(y-a)

=======
Suggestion 3

def main():
    input_line = input()
    input_line = input_line.split(' ')
    a = int(input_line[0])
    b = int(input_line[1])
    if a < 1 or a >= b or b >= 499500:
        print("输入不合法")
        return
    #求出塔的总高度
    total_height = int((1 + 999) * 999 / 2)
    #求出雪覆盖的高度
    snow_height = total_height - (b - a)
    #求出雪覆盖的深度
    snow_depth = b - a - snow_height + 1
    print(snow_depth)

=======
Suggestion 4

def snow(a, b):
    total = (b - a + 1) * (a + b) // 2
    return total - b

print(snow(8, 13))
print(snow(54, 65))

=======
Suggestion 5

def problem099_b():
    pass

=======
Suggestion 6

def get_n(n):
    return int((1+n)*n/2)

=======
Suggestion 7

def solve(a, b):
    return (b-a)*(b-a+1)//2 - b

=======
Suggestion 8

def main():
    #a,b = map(int, input().split())
    a,b = 8, 13
    print(b-a)

=======
Suggestion 9

def calc_snow_cover(a,b):
    #print("a,b",a,b)
    #print("a,b",a,b)
    #print("b-a",b-a)
    #print("b-a+1",b-a+1)
    #print("b-a+1//2",(b-a+1)//2)
    return (b-a+1)//2
