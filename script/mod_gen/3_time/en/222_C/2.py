def get_winner(a,b):
    if (a == "G" and b == "C") or (a == "C" and b == "P") or (a == "P" and b == "G"):
        return 0
    elif (a == "G" and b == "P") or (a == "C" and b == "G") or (a == "P" and b == "C"):
        return 1
    elif a == b:
        return 2

if __name__ == '__main__':
    get_winner()