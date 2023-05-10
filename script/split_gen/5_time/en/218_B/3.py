def main():
    p = list(map(int,input().split()))
    alpha = [chr(i) for i in range(ord('a'),ord('z')+1)]
    for i in range(26):
        print(alpha[p[i]-1],end='')
    print()
