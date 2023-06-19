def main():
    a,b,w = map(int,input().split())
    w = w*1000
    min_num = 0
    max_num = 0
    for i in range(a,b+1):
        if w%i==0:
            min_num = w//i
            break
    for i in range(b,a-1,-1):
        if w%i==0:
            max_num = w//i
            break
    if min_num==0 or max_num==0:
        print('UNSATISFIABLE')
    else:
        print(min_num,max_num)
