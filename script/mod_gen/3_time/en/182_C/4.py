def main():
    N = input()
    k = len(N)
    N = int(N)
    sum = 0
    for i in range(k):
        sum += int(N % 10)
        N = int(N / 10)
    if sum % 3 == 0:
        print(0)
    elif sum % 3 == 1:
        if k == 1:
            print(-1)
        elif k == 2:
            print(1)
        else:
            if N % 3 == 0:
                print(1)
            else:
                print(2)
    else:
        if k == 1:
            print(-1)
        elif k == 2:
            print(1)
        else:
            if N % 3 == 1:
                print(1)
            else:
                print(2)
main()
I'm new to python and I can't figure out how to get the program to run. I've tried running it in the terminal and in the python shell and nothing happens. What am I doing wrong? Thanks!
I'm not sure what you mean by "nothing happens". If you're running it in the terminal, you need to run it with python3. If you're running it in the python shell, you need to run it with python3 -i problems182_c.py . If you're running it in an IDE, you need to run it from the IDE.
If you're on Windows, you can run it with python problems182_c.py . If you're on Linux, you can run it with python3 problems182_c.py . If you're on Mac, you can run it with python3 problems182_c.py . If you're on any of those systems and you have multiple versions of Python installed, you can run it with python3.7 problems182_c.py .
If you're on Windows, you can run it with python problems182_c.py . If you're on Linux, you can run it with python3 problems182_c.py . If you're on Mac, you can run it with python3 problems182_c.py . If you're on any of those systems and you have multiple versions of Python installed, you can run it with python3.7 problems182_c.py .
If you're on Windows, you can run it with python problems182_c.py . If you're on Linux, you can run it with python3 problems182_c.py .

if __name__ == '__main__':
    main()