def problem218_b():
    p = list(map(int, input().split()))
    s = ''
    for i in p:
        s += chr(i + 96)
    print(s)
