def check(s):
    if s.count("H") == 1 and s.count("2B") == 1 and s.count("3B") == 1 and s.count("HR") == 1:
        return "Yes"
    else:
        return "No"
s = [input() for i in range(4)]
print(check(s))

if __name__ == '__main__':
    check()