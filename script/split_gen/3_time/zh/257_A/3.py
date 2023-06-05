def main():
    x = input()
    n = int(x.split()[0])
    x = int(x.split()[1])
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(alphabet[(x-1)//n])
