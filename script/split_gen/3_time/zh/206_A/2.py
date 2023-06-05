def problem206_a():
    N = int(input())
    if N * 1.08 < 206:
        print("Yay!")
    elif N * 1.08 == 206:
        print("so-so")
    else:
        print(":(")
