def main():
    a,b,c = map(int,input().split())
    flag = 0
    for i in range(a,b+1):
        if i%c == 0:
            print(i)
            flag = 1
            break
    if flag == 0:
        print(-1)
