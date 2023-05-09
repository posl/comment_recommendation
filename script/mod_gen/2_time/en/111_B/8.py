def main():
    N = int(input())
    if N%111 == 0:
        print(N)
    else:
        print(((N//111)+1)*111)
main()
I was wondering if there was a better way to do this, as I feel like my solution is a bit messy. I'm also wondering if there is a way to do this without using any if statements.
I'm just starting out with Python so any help would be greatly appreciated. Thanks!
I'm trying to write a program that will print the first 100 prime numbers. I've got it working, but I'm not sure if there is a more efficient way to do it. Here's what I've got so far:

if __name__ == '__main__':
    main()