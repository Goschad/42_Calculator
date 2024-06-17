import utils.color as color
import utils.get_info as get_info
import utils.convert as convert

if __name__ == '__main__':
    color.header()
    try:
        lvl = get_info.set_level()
        current_xp = convert.convert_lvl_to_xp(lvl)
        added_xp = get_info.set_xp()
        n_lvl = convert.convert_xp_to_level(current_xp + added_xp)
        print("You will be lvl " + f"{color.GREEN}" + n_lvl + f"{color.RESET}")
    except KeyboardInterrupt:
        print('')
    except:
        print(get_info._INPUT_ERROR)

# add blackhole https://medium.com/@benjaminmerchin/42-black-hole-deep-dive-cbc4b343c6b2
