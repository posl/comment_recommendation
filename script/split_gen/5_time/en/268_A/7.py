def main():
    x = input()
    x = x.split()
    x = [int(x) for x in x]
    x = set(x)
    print(len(x))
