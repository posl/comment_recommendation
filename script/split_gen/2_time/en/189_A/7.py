def main():
    c = input()
    print("Won" if len(set(c)) == 1 else "Lost")
