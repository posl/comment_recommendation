def main():
    # Read from Standard Input
    s = [input() for i in range(10)]
    # Process
    for i in range(10):
        s[i] = s[i].replace(".", "0")
        s[i] = s[i].replace("#", "1")
        s[i] = int(s[i], 2)
    for a in range(10):
        for b in range(a, 10):
            for c in range(10):
                for d in range(c, 10):
                    if all(((s[i] >> d) & 1) == 0 for i in range(a, b+1)) and all(((s[i] >> j) & 1) == 1 for i in range(a, b+1) for j in range(c, d+1)):
                        print(a+1, b+1)
                        print(c+1, d+1)
                        exit()
