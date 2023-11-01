def main():
    # 读取输入
    A, B, C, D = map(int, input().split())
    if A > C:
        print('Takahashi')
    elif A < C:
        print('Aoki')
