def main():
    S = input()
    T = input()
    s = set(S)
    t = set(T)
    if len(s) == len(t):
        print("Yes")
    else:
        print("No")
