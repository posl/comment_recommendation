def main():
    # 读取输入
    s = []
    for i in range(4):
        s.append(input())
    # 判断是否有H、2B、3B和HR中的各一个
    if 'H' in s and '2B' in s and '3B' in s and 'HR' in s:
        print('Yes')
    else:
        print('No')
