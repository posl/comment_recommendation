def main():
    n = int(input())
    s = input()
    # ord('A') = 65, ord('Z') = 90
    # chr(65) = 'A', chr(90) = 'Z'
    # ord('A') - ord('A') = 0
    # ord('Z') - ord('A') = 25
    # ord('A') + 1 = 66
    # chr(66) = 'B'
    for c in s:
        # ord(c) + n が ord('Z') より大きいときは、ord('A') + (ord(c) + n - ord('Z') - 1) とする。
        print(chr(ord('A') + (ord(c) + n - ord('A')) % 26), end='')
    print('')
