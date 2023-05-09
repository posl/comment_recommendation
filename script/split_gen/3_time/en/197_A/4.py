def main():
    s = list(input())
    s.append(s.pop(0))
    print("".join(s))
