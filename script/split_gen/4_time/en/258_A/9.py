def solve(K: int):
    print('{:02d}:{:02d}'.format(*divmod((K + 21 * 60) % (24 * 60), 60)))
