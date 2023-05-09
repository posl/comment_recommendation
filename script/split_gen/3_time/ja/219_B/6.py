def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    ans = ''
    for i in range(len(T)):
        if T[i] == '1':
            ans += S1
        elif T[i] == '2':
            ans += S2
        else:
            ans += S3
    print(ans)
