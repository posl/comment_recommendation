def main():
    s = input()
    if s[0] == 'o':
        ans = 1
    elif s[0] == 'x':
        ans = 0
    else:
        ans = 9
    for i in range(1, 10):
        if s[i] == 'o':
            ans *= 1
        elif s[i] == 'x':
            ans *= 0
        else:
            ans *= 9
    print(ans)
