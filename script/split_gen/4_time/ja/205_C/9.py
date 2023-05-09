def main():
    #n = int(input())
    #s = input()
    #n, k = map(int, input().split())
    a, b, c = map(int, input().split())
    #al = list(map(int, input().split()))
    #a = [int(input()) for i in range(n)]
    #a = [list(map(int, input().split())) for i in range(n)]
    #print(n, k)
    #print(a)
    #print(al)
    #print(a)
    #print(b)
    #print(c)
    if c % 2 == 0:
        a = abs(a)
        b = abs(b)
    if a == b:
        print('=')
    elif a > b:
        print('>')
    else:
        print('<')
    return
