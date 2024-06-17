from utils.get_info import level_xp_required

def convert_lvl_to_xp(lvl):
    xp = level_xp_required[int(lvl[0])]
    if len(lvl) == 2:
        xp += ((level_xp_required[int(lvl[0]) + 1] - level_xp_required[int(lvl[0])]) / 100) * int(lvl[1])
    return round(xp)

def convert_xp_to_level(xp):
    lvl = 0
    count = 0
    per = 0
    while count <= 30:
        if count == 30:
            return 30
        if xp == level_xp_required[count]:
            lvl = count
            break
        if xp < level_xp_required[count]:
            lvl = count - 1
            break
        count += 1
    count = 0
    xp = xp - level_xp_required[lvl]
    percent = (level_xp_required[lvl + 1] - level_xp_required[lvl]) / 100
    while per + percent < xp:
        count += 1
        per += percent
    if count > 9:
        n_lvl = str(lvl) + '.' + str(count)
    else:
        n_lvl = str(lvl) + '.0' + str(count)
    return n_lvl
