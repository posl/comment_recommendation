def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n-2):
        if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
            count += 1
    print(count)
main()
The solution is very simple. It is just a matter of counting the number of times ABC occurs in the string.
