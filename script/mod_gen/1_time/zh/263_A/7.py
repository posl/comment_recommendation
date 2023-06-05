def main():
    # 读入数据
    A, B, C, D, E = map(int, input().split())
    # 判断是否为满堂红
    if A == B == C or A == B == D or A == B == E or A == C == D or A == C == E or A == D == E or B == C == D or B == C == E or B == D == E or C == D == E:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()