def main():
    a,b,c = map(int,input().split())
    if b >= min(a,c) and b <= max(a,c):
        print('是')
    else:
        print('没有')
