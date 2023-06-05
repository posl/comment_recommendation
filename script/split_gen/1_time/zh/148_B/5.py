def main():
    # N = int(input())
    # s, t = input().split()
    N = 8
    s = "hmhmnknk"
    t = "uuuuuuuu"
    result = ""
    for i in range(N):
        result += s[i] + t[i]
    print(result)
