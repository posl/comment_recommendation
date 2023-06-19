def main():
    s = input()
    print(s.rfind('a') + 1 if 'a' in s else -1)
