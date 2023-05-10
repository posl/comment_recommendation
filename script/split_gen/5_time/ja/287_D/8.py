def solve():
    s = input()
    t = input()
    # tの?をaに置き換えた文字列を作成
    t_list = list(t)
    for i in range(len(t)):
        if t_list[i] == '?':
            t_list[i] = 'a'
    t_a = ''.join(t_list)
    # sの先頭からtの長さ分の文字列を作成
    s_a = s[:len(t)]
    # tの?をaに置き換えた文字列とsの先頭からtの長さ分の文字列が一致したらYes
    if s_a == t_a:
        print('Yes')
    else:
        print('No')
    # sの先頭からtの長さ分の文字列を作成
    s_b = s[-len(t):]
    # tの?をaに置き換えた文字列とsの末尾からtの長さ分の文字列が一致したらYes
    if s_b == t_a:
        print('Yes')
    else:
        print('No')
