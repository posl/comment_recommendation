def main():
    n = int(input())
    if int(1.08 * n) < 206:
        print("Yay!")
    elif int(1.08 * n) == 206:
        print("so-so")
    else:
        print(":(")
