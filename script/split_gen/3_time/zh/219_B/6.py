def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = ''
    for i in t:
        if i == '1':
            ans = ans + s1
        elif i == '2':
            ans = ans + s2
        else:
            ans = ans + s3
    print(ans)
