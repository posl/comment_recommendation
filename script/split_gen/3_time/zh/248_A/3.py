def problem248_a():
    s = input()
    s = list(s)
    s.sort()
    for i in range(10):
        if str(i) not in s:
            print(i)
            break
problem248_a()
