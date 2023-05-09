def main():
    s = input()
    q = int(input())
    ans = s
    reverse = False
    for _ in range(q):
        t = input()
        if t == '1':
            reverse = not reverse
        else:
            _, f, c = t.split()
            if (f == '1') ^ reverse:
                ans = c + ans
            else:
                ans = ans + c
    if reverse:
        ans = ans[::-1]
    print(ans)
