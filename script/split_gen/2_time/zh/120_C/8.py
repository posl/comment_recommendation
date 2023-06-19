def main():
    S = input()
    n = len(S)
    red = 0
    blue = 0
    for i in range(n):
        if S[i] == '0':
            red += 1
        else:
            blue += 1
    print(2 * min(red, blue))
