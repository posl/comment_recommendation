def main():
    a = int(input())
    if a == 0:
        print("21:00")
    elif a >= 1 and a <= 60:
        print("21:%02d" % a)
    elif a >= 61 and a <= 99:
        print("22:%02d" % (a - 60))
    elif a == 100:
        print("22:40")
main()
The solution is pretty straight forward. You just need to make sure you follow the constraints. I used the %02d format to make sure that the output is always two digits. Otherwise, you will get an incorrect answer.
