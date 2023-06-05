def main():
    n = int(input())
    if n < 16:
        print("0" + hex(n)[2:].upper())
    else:
        print(hex(n)[2:].upper())
