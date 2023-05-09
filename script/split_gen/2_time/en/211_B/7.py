def main():
    s = [input() for i in range(4)]
    if len(set(s)) == 4:
        print("Yes")
    else:
        print("No")
