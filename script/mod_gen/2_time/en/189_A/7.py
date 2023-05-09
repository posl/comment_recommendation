def main():
    c = input()
    print("Won" if len(set(c)) == 1 else "Lost")

if __name__ == '__main__':
    main()