def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    dic = {'1': s1, '2': s2, '3': s3}
    ans = ''
    for i in t:
        ans += dic[i]
    print(ans)
