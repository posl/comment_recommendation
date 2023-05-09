def main():
    s = input()
    w = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    print(w.index('Saturday') - w.index(s))

if __name__ == '__main__':
    main()