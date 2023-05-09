def main():
    n = int(input())
    n = str(n)
    x = ""
    for i in n:
        if i == "1":
            x += "9"
        elif i == "9":
            x += "1"
    print(x)
