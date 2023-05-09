def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    s = input()
    result = 0
    for i in range(5):
        if s == days[i]:
            result = 5 - i
            break
    print(result)
main()

if __name__ == '__main__':
    main()