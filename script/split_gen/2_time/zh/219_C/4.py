def main():
    s1 = input()
    s2 = input()
    s3 = input()
    T = input()
    ans = ''
    for i in range(len(T)):
        if T[i] == '1':
            ans += s1
        elif T[i] == '2':
            ans += s2
        elif T[i] == '3':
            ans += s3
    print(ans)
