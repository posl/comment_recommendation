def reverse(a):
    return 7-a
a,b,c = map(int,input().split())
print(reverse(a)+reverse(b)+reverse(c))

if __name__ == '__main__':
    reverse()