def main():
    x_y = input()
    x = x_y.split(".")[0]
    y = x_y.split(".")[1]
    if y <= "2":
        print(x + "-")
    elif y <= "6":
        print(x)
    else:
        print(x + "+")
