def main():
    a,b,c,d,e,f,x = map(int, input().split())
    takahashi = 0
    aoki = 0
    # 高桥和青木同时开始慢跑
    for i in range(x):
        if i % (a + b) < a:
            takahashi += 1
        if i % (d + e) < d:
            aoki += 1
    # 高桥和青木谁走在前面
    if takahashi > aoki:
        print('高桥')
    elif takahashi < aoki:
        print('青木')
    else:
        print('画')
