def main():
    a,b,c = map(int,input().split())
    if b>a and b<c or b<a and b>c:
        print('是')
    else:
        print('没有')
