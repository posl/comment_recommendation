def main():
    a = input()
    a = a.split()
    a = list(map(int, a))
    print(min(a))
