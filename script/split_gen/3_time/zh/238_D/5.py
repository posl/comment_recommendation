def main():
    t = int(input())
    for i in range(t):
        a,s = input().split()
        a = int(a)
        s = int(s)
        if a > s:
            print('No')
        else:
            if (s-a)%2 == 0:
                print('Yes')
            else:
                print('No')
