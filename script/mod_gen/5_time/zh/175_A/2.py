def problem175_a():
    S = input()
    if S == "RRR":
        print(3)
    elif S == "RRS" or S == "SRR":
        print(2)
    elif S == "SSS":
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    problem175_a()