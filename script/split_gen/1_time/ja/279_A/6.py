def main():
    S = input()
    v = 0
    w = 0
    for s in S:
        if s == "v":
            v += 1
        else:
            w += 1
    print(v * w)
