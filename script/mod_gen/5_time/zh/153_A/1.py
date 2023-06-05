def attack(hp, at):
    if hp % at == 0:
        return hp // at
    else:
        return hp // at + 1

if __name__ == '__main__':
    attack()