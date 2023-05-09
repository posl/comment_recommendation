def check_pin(pin):
    if pin[0] == pin[1] == pin[2] == pin[3]:
        return "Weak"
    elif (int(pin[0]) == (int(pin[1]) - 1) % 10) and (int(pin[1]) == (int(pin[2]) - 1) % 10) and (int(pin[2]) == (int(pin[3]) - 1) % 10):
        return "Weak"
    else:
        return "Strong"
pin = input()
print(check_pin(pin))
I am a 3rd year student of Computer Science and Engineering at the University of Moratuwa. I am currently doing my internship at the University of Moratuwa.
