def changeN(n):
    s = str(n)
    ans = ""
    for i in s:
        if i == "1":
            ans += "9"
        elif i == "9":
            ans += "1"
    return int(ans)

if __name__ == '__main__':
    changeN()