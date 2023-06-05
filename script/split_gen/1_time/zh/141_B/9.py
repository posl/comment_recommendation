def main():
    s=input()
    flag=True
    for i in range(len(s)):
        if i%2==0:
            if s[i] not in ['R','U','D']:
                flag=False
                break
        else:
            if s[i] not in ['L','U','D']:
                flag=False
                break
    if flag:
        print('Yes')
    else:
        print('No')
