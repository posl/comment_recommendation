def main():
    n = int(input())
    ans = False
    for i in range(0, n+1, 4):
        if (n-i)%7 == 0:
            ans = True
            break
    if ans:
        print('Yes')
    else:
        print('No')
