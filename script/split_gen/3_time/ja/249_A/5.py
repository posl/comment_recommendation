def jog(a, b, c, d, e, f, x):
    takahashi = 0
    aoki = 0
    for i in range(x):
        if i % (a + c) < a:
            takahashi += b
        if i % (d + f) < d:
            aoki += e
    if takahashi > aoki:
        print('Takahashi')
    elif takahashi < aoki:
        print('Aoki')
    else:
        print('Draw')
