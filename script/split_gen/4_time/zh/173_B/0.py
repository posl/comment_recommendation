def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print("AC x", s.count("AC"))
    print("WA x", s.count("WA"))
    print("TLE x", s.count("TLE"))
    print("RE x", s.count("RE"))
