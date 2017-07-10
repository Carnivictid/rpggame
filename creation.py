troubled_trader_dict = {'Troubled Trader': 'A trader asked you to clear his warehouse of an evil.'}
the_cript_dict = {'The Crypt': 'The town mayor asked you to cleanse the crypt'}
quest_list_dict = {}

print(quest_list_dict)
quest_list_dict.update(the_cript_dict)
quest_list_dict.update(troubled_trader_dict)
for val in quest_list_dict.items():
        print(val)
