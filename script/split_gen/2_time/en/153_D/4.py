def main():
    H = int(input())
    ans = 0
    while H > 0:
        ans += 2 ** (H.bit_length() - 1)
        H -= 2 ** (H.bit_length() - 1)
    print(ans)
