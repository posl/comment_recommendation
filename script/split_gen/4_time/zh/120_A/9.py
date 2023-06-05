def main():
    # 读入数据
    a,b,c = map(int, input().split())
    ans = min(b//a, c)
    print(ans)
