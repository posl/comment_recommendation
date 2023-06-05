def main():
    n = int(input())
    if n*1.08 < 206:
        print("Yay!")
    elif n*1.08 == 206:
        print("so-so")
    else:
        print(":(")
