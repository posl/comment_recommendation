def main():
    s = input()
    print(min(s.count("0"), s.count("1")) * 2)
