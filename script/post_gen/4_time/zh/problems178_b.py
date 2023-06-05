Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,d = map(int, input().split())
    print(max(a*c, a*d, b*c, b*d))

=======
Suggestion 2

def get_max(a,b,c,d):
    x = [a,b]
    y = [c,d]
    max_x = max(x)
    min_x = min(x)
    max_y = max(y)
    min_y = min(y)
    if max_x * max_y >= max_x * min_y:
        if max_x * max_y >= min_x * max_y:
            if max_x * max_y >= min_x * min_y:
                return max_x * max_y
            else:
                return min_x * min_y
        else:
            if min_x * max_y >= min_x * min_y:
                return min_x * max_y
            else:
                return min_x * min_y
    else:
        if min_x * max_y >= min_x * min_y:
            if min_x * max_y >= max_x * min_y:
                return min_x * max_y
            else:
                return max_x * min_y
        else:
            if min_x * min_y >= max_x * min_y:
                return min_x * min_y
            else:
                return max_x * min_y

=======
Suggestion 3

def maxProduct(a, b, c, d):
    if a < 0 and b > 0:
        if c < 0 and d > 0:
            return max(a * c, a * d, b * c, b * d)
        else:
            return max(a * c, a * d, b * c, b * d, a * b)
    elif a < 0 and b <= 0:
        if c < 0 and d > 0:
            return max(a * c, a * d, b * c, b * d)
        else:
            return max(a * c, a * d, b * c, b * d, a * b)
    elif a >= 0 and b > 0:
        if c < 0 and d > 0:
            return max(a * c, a * d, b * c, b * d)
        else:
            return max(a * c, a * d, b * c, b * d, a * b)
    elif a >= 0 and b <= 0:
        if c < 0 and d > 0:
            return max(a * c, a * d, b * c, b * d)
        else:
            return max(a * c, a * d, b * c, b * d, a * b)

=======
Suggestion 4

def max_product(a,b,c,d):
    max = a * c
    if a * d > max:
        max = a * d
    if b * c > max:
        max = b * c
    if b * d > max:
        max = b * d
    return max

=======
Suggestion 5

def solve(a,b,c,d):
    max = 0
    for i in range(a,b+1):
        for j in range(c,d+1):
            if i*j > max:
                max = i*j
    return max
