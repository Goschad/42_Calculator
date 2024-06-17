_INPUT_ERROR = "\033[31mError\033[0m: this input is not valid."
 
level_xp_required = [0, 462, 2688, 5885, 11777, 29217, 46255,
                     63559, 74340, 85483, 95000, 105630,
                     124446, 145782, 169932, 197316, 228354,
                     263508, 303366, 348516, 399672, 457632,
                     523320, 597786, 682164, 777756, 886074,
                     1008798, 1147902, 1305486, 1484070]

def set_level():
    level = str(input("Current level : "))
    tab = level.split(".")
    if not tab[0].isdigit():
        print(_INPUT_ERROR)
        raise
    if len(tab) == 2:
        if not tab[1].isdigit() > 0:
            print(_INPUT_ERROR)
            raise
        if int(tab[1]) < 10 and not tab[1][0] == '0':
            tab[1] += '0'
    return tab

def set_xp():
    xp = int(input("XP : "))
    if xp < 0:
        raise
    return xp

def set_coalitions():
    bol = bool(input("Coalitions bonus : "))
    return bol