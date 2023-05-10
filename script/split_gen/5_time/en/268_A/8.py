def main():
    a = input().split()
    a = list(dict.fromkeys(a))
    print(len(a))
