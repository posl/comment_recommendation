def main():
    S = input()
    x = 0
    for i in range(4):
        if S[i] == "+":
            x += 1
        else:
            x -= 1
    print(x)
