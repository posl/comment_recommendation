def problems247_a():
    S = str(input())
    s = list(S)
    s.append(s[0])
    s.pop(0)
    print("".join(s))

if __name__ == '__main__':
    problems247_a()