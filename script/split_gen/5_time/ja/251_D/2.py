def main():
    w = int(input())
    if w <= 2:
        print('NO')
        return
    if w % 2 == 0:
        print('YES')
    else:
        print('NO')
