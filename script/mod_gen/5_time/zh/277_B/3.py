def main():
    n = int(input())
    s = [input() for i in range(n)]
    if len(s) == len(set(s)):
        if all(s[i][0] in 'HDCS' and s[i][1] in 'A23456789TJQK' for i in range(n)):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
main()
