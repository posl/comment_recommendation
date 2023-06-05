def problem206_a():
    n = int(input())
    if n * 1.08 < 206:
        print("Yay!")
    elif n * 1.08 > 206:
        print(":(")
    else:
        print("so-so")
