def main():
    s = input()
    s = s.replace(s, 'x' * len(s))
    print(s)
