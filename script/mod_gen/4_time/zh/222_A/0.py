def problem222_a(n):
    if n < 0 or n > 9999:
        print('error')
        return
    print('{:0>4d}'.format(n))
problem222_a(321)
problem222_a(7777)
problem222_a(1)
problem222_a(10000)
problem222_a(-1)
