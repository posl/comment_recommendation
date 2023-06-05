def main():
    n = int(input())
    s = input()
    q = int(input())
    is_reverse = False
    left = s[:n]
    right = s[n:]
    for i in range(q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            if is_reverse:
                if a >= n:
                    a -= n
                else:
                    a += n
                if b >= n:
                    b -= n
                else:
                    b += n
            left = left[:a] + right[b] + left[a+1:]
            right = right[:b] + left[a] + right[b+1:]
        else:
            is_reverse = not is_reverse
    if is_reverse:
        left, right = right, left
    print(left + right)
