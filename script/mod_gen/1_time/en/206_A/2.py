def main():
    N = int(input())
    if N * 108 < 20600:
        print("Yay!")
    elif N * 108 == 20600:
        print("so-so")
    else:
        print(":(")
main()
I am using Python 3.4.3 and I am getting the following error:
Traceback (most recent call last):
  File "problems206_a.py", line 31, in <module>
    main()
  File "problems206_a.py", line 29, in main
    print("so-so")
UnicodeEncodeError: 'ascii' codec can't encode character '\u2212' in position 0: ordinal not in range(128)
I am not sure how to fix this. I have tried to add the following line to the top of the file:

if __name__ == '__main__':
    main()