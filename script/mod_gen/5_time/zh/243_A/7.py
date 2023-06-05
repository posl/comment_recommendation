def problem243_a():
    v,a,b,c=map(int,input().split())
    while v>=0:
        v-=a
        if v<0:
            print('F')
            break
        v-=b
        if v<0:
            print('M')
            break
        v-=c
        if v<0:
            print('T')
            break

if __name__ == '__main__':
    problem243_a()