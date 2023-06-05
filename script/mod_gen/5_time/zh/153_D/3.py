def solve():
    h = int(input())
    print(2**(h.bit_length())-1)

if __name__ == '__main__':
    solve()