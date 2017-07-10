from collections import OrderedDict
import playeractions
from players import Player
import world, os, time, sys, cinematics, textwrap


def play():
    # The world itself is generated from the map.py module.
    world.parse_world_dsl()
    
    # The player class is initialized.
    player = Player("You", 4)
    player.refresh_level()
    steven = Player("Steven", 5)
    steven.refresh_level()
    player.party.append(steven)

    # The game loop begins. Looks to see if the game has been won.
    while not player.victory:
    
        # The player's current tile is called.
        room = world.tile_at(player.x, player.y)
        
        # The room's intro text plays. Once per entrance into the tile.
        print(room.intro_text())
        
        # Then the action loop begins.
        while player.is_alive():
            
            # The title text plays to remind player which tile they are in.
            print(room.title_text())
            
            # The room modify_player function runs. Will be changed.
            room.modify_player(player)
            
            # A check to make sure user is alive, and game is not won.
            if player.is_alive() and not player.victory:
            
                # The playeractions list is called here. 
                choose_action(room, player)
                player.party_decision(room)
                
                # Now we are checking to see if we are in the same room.
                check_room = world.tile_at(player.x, player.y)
                
                # Now we give the AI party members a chance.
                #player.party_decision(room)
                
                # If we change rooms, we break the loop to grab the new room.
                if check_room != room:
                    break
            
            # If the player dies, the game over text appears.
            elif not player.is_alive():
                print("\nYour journey has come to an early end! But it's not over yet.")


def choose_action(room, player):
    action = None
    while not action:
        available_actions = playeractions.get_available_actions(room, player)
        action_input = input("\nAction: ")
        action = available_actions.get(action_input)

        # If an action is type out, this will always run.
        if action:
            action()

        # Now begins the fully typed commands.
        elif action_input == 'help':
            print("\nThere are several commands you can use at any time! Be careful, they take 1 round.")
            print("\nCommands:")
            print("\nwait: waits for 1 round.")
            print("\nparty: opens the party management window.")
            print("\nmore commands comming soon.")
            print("\n")
        elif action_input == 'party':
            print("\nThis command is a work in progress. Sorry!")
            break
        elif action_input == 'wait':
            print("\nYou wait for one round.")
            break
        else:
            print("""
        Invalid action!
            """)

play()















































