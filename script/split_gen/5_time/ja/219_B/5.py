def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    ans = ''
    for i in T:
        if i == '1':
            ans += S1
        elif i == '2':
            ans += S2
        elif i == '3':
            ans += S3
    print(ans)
