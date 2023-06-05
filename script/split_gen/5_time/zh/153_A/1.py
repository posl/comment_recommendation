def attack(hp, at):
    if hp % at == 0:
        return hp // at
    else:
        return hp // at + 1
