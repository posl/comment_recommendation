def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    T = input()
    result = ""
    for t in T:
        if t == "1":
            result += S_1
        elif t == "2":
            result += S_2
        else:
            result += S_3
    print(result)
