def main():
    s = input()
    print(min(s[i:] + s[:i] for i in range(len(s))))

if __name__ == '__main__':
    main()