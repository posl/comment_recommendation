def dogname(n):
    if n<=26:
        return chr(n+96)
    elif n<=702:
        return chr(n//26+96)+chr(n%26+96)
    elif n<=18278:
        return chr(n//702+96)+chr(n//26%26+96)+chr(n%26+96)
    elif n<=475254:
        return chr(n//18278+96)+chr(n//702%26+96)+chr(n//26%26+96)+chr(n%26+96)
    elif n<=12356630:
        return chr(n//475254+96)+chr(n//18278%26+96)+chr(n//702%26+96)+chr(n//26%26+96)+chr(n%26+96)
    elif n<=321272406:
        return chr(n//12356630+96)+chr(n//475254%26+96)+chr(n//18278%26+96)+chr(n//702%26+96)+chr(n//26%26+96)+chr(n%26+96)
    elif n<=8451004008:
        return chr(n//321272406+96)+chr(n//12356630%26+96)+chr(n//475254%26+96)+chr(n//18278%26+96)+chr(n//702%26+96)+chr(n//26%26+96)+chr(n%26+96)
    elif n<=222651511842:
        return chr(n//8451004008+96)+chr(n//321272406%26+96)+chr(n//12356630%26+96)+chr(n//475254%26+96)+chr(n//18278%26+96)+chr(n//702%26+96)+chr(n//26%26+96)+chr(n%26+96)
    elif n<=5843183014110:
        return chr(n//222651511842+96)+chr(n//8451004008%26+96)+chr(n//321272406%26+96)+chr(n//12356630%26+96)+chr(n//475254%26+96)+chr(n//18278%26+96)+chr(n//702%26+96)+chr(n//26%26+96)+chr(n%26+96)
    elif n<=153

if __name__ == '__main__':
    dogname()