def main():
    x,y = map(int,input().split())
    if x>0 and y>0:
        print('合金')
    elif x==0 and y>0:
        print('银')
    elif x>0 and y==0:
        print('黄金')
