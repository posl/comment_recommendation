def main():
    N = input()
    if len(N) == 4:
        print(N)
    elif len(N) == 3:
        print("0" + N)
    elif len(N) == 2:
        print("00" + N)
    elif len(N) == 1:
        print("000" + N)
