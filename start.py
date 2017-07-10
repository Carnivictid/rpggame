from game import play


def start_screen():
    print("\nWelcome to Eternal Slumber, a D&D inspired adventure.")
    print("\nNow you will be making your Character")
    print("Right now, you can only be a fighter, but a Rogue will be added soon")
    print("\nPress Enter to continue")
    choice = input()


def run():

    start_screen()

    str_choice = 0
    dex_choice = 0
    con_choice = 0

    base_str = 8
    base_dex = 8
    base_con = 8

    buy_points = 16
    points_left = 0

    print("Also, currently, CHA, WIS, and INT have no use. So it is a 16 point buy")
    print("You will need to choose where you put your points. The base is 8")
    print("The options are Strength (hit harder, more often)"
          ", Dex (Better AC, to a point), or Con (Better HP)")
    ready = False
    while not ready:
        str_chosen = False
        dex_chosen = False
        con_chosen = False

        while not str_chosen:
            try:
                str_choice = input("How many points to Strength? (hit harder, and more often)\n> ")
            except (ValueError, AttributeError):
                print("That was not a correct value")
            if int(str_choice) > 8:
                print("That is too high, try again.")
            buy_points = buy_points - int(str_choice)
            print("You chose to put {} points into Strength for {} Str total "
                  "You have {} points left".format(str_choice, (int(str_choice) + base_str), buy_points))
            str_chosen = True

        while not dex_chosen:
            try:
                dex_choice = input("How many points to Dex? (Better AC, to a point)\n> ")
            except (ValueError, AttributeError):
                print("That was not a correct value")
            if int(dex_choice) > 8:
                print("That is too high, try again.")
            points_left = buy_points - int(dex_choice)
            print("You chose to put {} points into Dex for {} Dex total "
                  "You have {} points left".format(dex_choice, (int(dex_choice) + base_dex), points_left))
            dex_chosen = True

        while not con_chosen:
            try:
                con_choice = input("How many points to Con? (Better HP)\n> ")
            except (ValueError, AttributeError):
                print("That was not a correct value")
            if int(con_choice) > 8:
                print("That is too high, try again.")
            points_left = buy_points - int(con_choice)
            print("You chose to put {} points into Con for {} Con total "
                  "You have {} points left".format(con_choice, (int(con_choice) + base_con), points_left))
            con_chosen = True
        ready = True

    print("\nYou chose {} Str, {} Dex, {} Con".format(str_choice, dex_choice, con_choice))
    print("For a total of {} Str, {} Dex, {} Con".format((int(str_choice) + base_str), (int(dex_choice) + base_dex), (int(con_choice) + base_con)))


    str_score = (int(str_choice) + base_str)
    dex_score = (int(dex_choice) + base_dex)
    con_score = (int(con_choice) + base_con)

    play()


# run()
