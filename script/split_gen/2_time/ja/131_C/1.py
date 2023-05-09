def main():
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
    A, B, C, D = map(int, input().split())
    # A 以上 B 以下の整数のうち、C でも D でも割り切れないものの個数を求めてください。
    print(B - A + 1 - (B // C - (A - 1) // C) - (B // D - (A - 1) // D) + (B // lcm(C, D) - (A - 1) // lcm(C, D)))
