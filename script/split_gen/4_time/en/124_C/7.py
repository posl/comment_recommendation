def main():
    s = input()
    print(min(s.count("01"), s.count("10")) * 2)
