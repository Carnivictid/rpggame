import os, sys, time, players


def cls():
    os.system("cls")


def delay_print(s, t):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(t)


def intro_cinematic():
    cls()
    time.sleep(3)
    delay_print('Hello...', 0.1)
    time.sleep(5)
    cls()
    delay_print('Do you know who I am?\n', 0.1)
    answer = input("\n> ")
    cls()
    if answer.lower() in ['y', 'yes', 'ye', 'yea', 'yeah', 'sure', 'ya']:
        time.sleep(2)
        delay_print('Yes? So you believe.', 0.1)
        time.sleep(5)
        cls()
    else:
        time.sleep(2)
        delay_print('No? Good.', 0.2)
        time.sleep(5)
        cls()
    time.sleep(2)
    delay_print('What is your name?\n\n> ', 0.1)
    time.sleep(8)
    cls()
    delay_print('I asked you... What is your name!?\n\n> ', 0.05)
    time.sleep(5)
    cls()
    delay_print('I do not have time for this... Sylrus, take him away. ', 0.1)
    time.sleep(5)
    delay_print('And kill him.', 0.1)
    time.sleep(3)
    cls()
    delay_print('Yes sir...', 0.1)
    time.sleep(2)
    cls()
    time.sleep(10)
    delay_print("Welcome to Eternal Slumber", .15)
    time.sleep(5)


def manhole_cinematic():
    cls()
    time.sleep(2)

    delay_print("You open the manhole cover, the light blinds you.\n"
                "The fresh air is almost intoxicating after the stench of the sewer.", 0.02)
    time.sleep(4)

    delay_print("\nYou climb out and are greeted with the sight of a large road,\n"
                "just south of what appears to be a coastal town.", 0.02)
    time.sleep(4)

    delay_print("\nThe manhole cover falls back into it's slot, seeming to be sealed.\n"
                "It looks like you can't get back into the sewer from here.", 0.02)
    time.sleep(4)

    delay_print("\nAs your eyesight adjusts, your headache clears.\n"
                "You feel as if this town can help you remember who you are.", 0.02)
    time.sleep(4)

    delay_print("\nYou hope...", 0.2)
    time.sleep(5)
    cls()
