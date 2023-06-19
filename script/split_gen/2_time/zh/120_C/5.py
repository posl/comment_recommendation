def main():
    S = input()
    red = 0
    blue = 0
    for i in range(len(S)):
        if S[i] == '0':
            red += 1
        else:
            blue += 1
    print(2 * min(red, blue))
