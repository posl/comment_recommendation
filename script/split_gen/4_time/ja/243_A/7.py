def problems243_a():
    V,A,B,C = map(int,input().split())
    if V % A == 0:
        print('T')
    elif V % B == 0:
        print('T')
    elif V % C == 0:
        print('T')
    elif V % A + V % B == 0:
        print('T')
    elif V % A + V % C == 0:
        print('T')
    elif V % B + V % C == 0:
        print('T')
    elif V % A + V % B + V % C == 0:
        print('T')
    else:
        print('F')
