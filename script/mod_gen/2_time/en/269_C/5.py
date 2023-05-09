def solve():
    N = int(input())
    if N == 0:
        print(0)
        return
    bit = bin(N)[2:]
    bit = bit[::-1]
    print(0)
    for i in range(len(bit)):
        if bit[i] == "1":
            print(1 << i)
    return

if __name__ == '__main__':
    solve()