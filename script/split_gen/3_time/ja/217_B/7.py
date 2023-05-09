def main():
    s = [input() for _ in range(3)]
    t = ["ABC", "ARC", "AGC", "AHC"]
    for i in s:
        t.remove(i)
    print(t[0])
