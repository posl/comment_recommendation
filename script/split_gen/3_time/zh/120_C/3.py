def main():
    s = input()
    #s = "11011010001011"
    #s = "0011"
    l = len(s)
    red = 0
    blue = 0
    for i in range(l):
        if s[i] == "0":
            red += 1
        else:
            blue += 1
    print(min(red, blue) * 2)
