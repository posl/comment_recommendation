def main():
    # Write code here 
    s = input()
    count = 0
    for i in range(10000):
        s1 = str(i).zfill(4)
        for j in range(10):
            if s[j] == 'o' and str(j) not in s1:
                break
            elif s[j] == 'x' and str(j) in s1:
                break
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()