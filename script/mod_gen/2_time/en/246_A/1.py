def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1
    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1
    print(x4, y4)
main()
I have a problem with the code. It is giving me a runtime error:
Traceback (most recent call last):
  File "problems246_a.py", line 40, in <module>
    main()
  File "problems246_a.py", line 38, in main
    x4, y4 = map(int, input().split())
ValueError: not enough values to unpack (expected 2, got 0)
I have tried to debug the code and it seems that the input is not being read correctly. I have tried to change the input() to raw_input() and it still gives me the same error. I have also tried to change the input to sys.stdin.readline() and it still gives me the same error.
Any help would be appreciated.
I have a problem with the code. It is giving me a runtime error: Traceback (most recent call last): File "problems246_a.py", line 40, in <module> main() File "problems246_a.py", line 38, in main x4, y4 = map(int, input().split()) ValueError: not enough values to unpack (expected 2, got 0) I have tried to debug the code and it seems that the input is not being read correctly. I have tried to change the input() to raw_input() and it still gives me the same error. I have also tried to change the input to sys.stdin.readline() and it still gives me the same error. Any help would be appreciated.
I think you are missing the newline character at the end of each line. When you use input() , it reads until the newline character. If you have a file with no newline characters at the end of each line, then you will get this error.
I think you are missing the newline

if __name__ == '__main__':
    main()