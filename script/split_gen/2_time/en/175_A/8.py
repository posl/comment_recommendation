def main():
    s = input()
    print(max(len(x) for x in s.split('S')))
