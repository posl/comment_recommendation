def main():
    S = input()
    mod = 10**9 + 7
    ABC = [0, 0, 0]
    ans = 1
    for s in S:
        if s == "?":
            ans *= 3
            ans %= mod
            ABC = [ABC[0] * 3 + ABC[1] + ABC[2], ABC[0] + ABC[1] * 3 + ABC[2], ABC[0] + ABC[1] + ABC[2] * 3]
            ABC = [a % mod for a in ABC]
        else:
            ABC = [ABC[0] + ABC[1] + ABC[2], ABC[0] + ABC[1] + ABC[2], ABC[0] + ABC[1] + ABC[2]]
            ABC[ord(s) - 65] += ans
            ABC = [a % mod for a in ABC]
    print(ABC[2])
