import re

class Pokemon:
    def __init__(self):
        self.moves = []
    def add_name(self, name):
        self.name = name.lower().replace(' ','-')
    def add_item(self, item):
        self.item = item.lower().replace(' ','-')
    def add_ability(self, ability):
        self.ability = ability.lower().replace(' ','-')
    def add_teratype(self, tera):
        self.tera = tera.lower().replace(' ','-')
    def add_move(self, move):
        self.moves.append(move.lower().replace(' ','-'))
    def __str__(self):
        all_moves = ""
        for x in self.moves:
            all_moves+=x.lower().replace(' ','-')+","
        all_moves = all_moves[:-1]
        return self.name +" @ "+ self.item + " ("+ self.ability +") [" + self.tera + "] -> " + all_moves


def upper_case_to_underscore(string):
    return re.sub( '(?<!^)(?=[A-Z])', '-', string).lower().replace('--', '-')


def parse_showdown_game(gameFile):
    # Process all games :)
    all_info = dict()

    is_valid = False
    player1 = ""
    elo1 = ""
    player2 = ""
    elo2 = ""
    winner = ""
    timeGame = ""
    tier = ""
    first_pokemon_player_1_a = ""
    first_move_player_1_a = ""
    first_pokemon_player_1_b = ""
    first_move_player_1_b = ""
    first_pokemon_player_2_a = ""
    first_move_player_2_a = ""
    first_pokemon_player_2_b = ""
    first_move_player_2_b = ""
    all_pokemon_player_1 = []
    all_pokemon_player_2 = []
    teams_processed = 0
    all_pokemons1 = []
    all_pokemons2 = []
    has_passed_turn = False
    has_started_game = False

    for line in gameFile:
        lineDetail = line.split("|")
        if len(lineDetail) == 1: continue

        if lineDetail[1] == "player":
            if lineDetail[2] == "p1" and player1 == "":
                player1 = lineDetail[3]
                elo1 = lineDetail[5].replace('\n', '')
            if lineDetail[2] == "p2" and player2 == "":
                player2 = lineDetail[3]
                elo2 = lineDetail[5].replace('\n', '')

        if lineDetail[1] == "turn":
            if lineDetail[2][:-1] == "1":
                has_started_game = True
            if lineDetail[2][:-1] == "2":
                has_passed_turn = True

        if lineDetail[1] == "t:" and timeGame == "": timeGame = lineDetail[2][:-1]

        if lineDetail[1] == "win" and winner == "": winner = lineDetail[2][:-1]
        if lineDetail[1] == "tier" and tier == "":
            tier = lineDetail[2][:-1]
            if 'VGC' not in tier: return None

        if lineDetail[1] == "switch":
            if lineDetail[2].split(":")[0] == "p1a" and first_pokemon_player_1_a == "":
                first_pokemon_player_1_a = lineDetail[3].split(",")[0].lower().replace(" ", "-")
                all_pokemon_player_1.append(first_pokemon_player_1_a)
            elif lineDetail[2].split(":")[0] == "p1a":
                all_pokemon_player_1.append(lineDetail[3].split(",")[0].lower().replace(" ", "-"))
            if lineDetail[2].split(":")[0] == "p1b" and first_pokemon_player_1_b == "":
                first_pokemon_player_1_b = lineDetail[3].split(",")[0].lower().replace(" ", "-")
                all_pokemon_player_1.append(first_pokemon_player_1_b)
            elif lineDetail[2].split(":")[0] == "p1b":
                all_pokemon_player_1.append(lineDetail[3].split(",")[0].lower().replace(" ", "-"))
            if lineDetail[2].split(":")[0] == "p2a" and first_pokemon_player_2_a == "":
                first_pokemon_player_2_a = lineDetail[3].split(",")[0].lower().replace(" ", "-")
                all_pokemon_player_2.append(first_pokemon_player_2_a)
            elif lineDetail[2].split(":")[0] == "p2a":
                all_pokemon_player_2.append(lineDetail[3].split(",")[0].lower().replace(" ", "-"))
            if lineDetail[2].split(":")[0] == "p2b" and first_pokemon_player_2_b == "":
                first_pokemon_player_2_b = lineDetail[3].split(",")[0].lower().replace(" ", "-")
                all_pokemon_player_2.append(first_pokemon_player_2_b)
            elif lineDetail[2].split(":")[0] == "p2b":
                all_pokemon_player_2.append(lineDetail[3].split(",")[0].lower().replace(" ", "-"))

        if lineDetail[1] == "move" and has_passed_turn == False:
            if lineDetail[2].split(": ")[0] == "p1a" and first_move_player_1_a == "":
                first_move_player_1_a = lineDetail[3]
            if lineDetail[2].split(": ")[0] == "p1b" and first_move_player_1_b == "":
                first_move_player_1_b = lineDetail[3]
            if lineDetail[2].split(": ")[0] == "p2a" and first_move_player_2_a == "":
                first_move_player_2_a = lineDetail[3]
            if lineDetail[2].split(": ")[0] == "p2b" and first_move_player_2_b == "":
                first_move_player_2_b = lineDetail[3]

        if lineDetail[1] == "showteam":
            is_valid = True
            if lineDetail[2] == 'p1':
                pokemon = Pokemon()
                pokemon.add_name(upper_case_to_underscore(lineDetail[3].replace(' ', '-')))
                pokemon.add_item(upper_case_to_underscore(lineDetail[5]))
                pokemon.add_ability(upper_case_to_underscore(lineDetail[6]))
                pokemon.add_teratype(lineDetail[14].split(']')[0].split(',')[-1].replace('\n', ''))
                pokemon.add_move(upper_case_to_underscore(lineDetail[7].split(',')[0]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[7].split(',')[1]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[7].split(',')[2]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[7].split(',')[3]))
                all_pokemons1.append(pokemon)

                pokemon = Pokemon()
                pokemon.add_name(upper_case_to_underscore(lineDetail[14].split(']')[1].replace(' ', '-')))
                pokemon.add_item(upper_case_to_underscore(lineDetail[16]))
                pokemon.add_ability(upper_case_to_underscore(lineDetail[17]))
                pokemon.add_teratype(lineDetail[25].split(']')[0].split(',')[-1].replace('\n', ''))
                pokemon.add_move(upper_case_to_underscore(lineDetail[18].split(',')[0]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[18].split(',')[1]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[18].split(',')[2]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[18].split(',')[3]))
                all_pokemons1.append(pokemon)

                pokemon = Pokemon()
                pokemon.add_name(upper_case_to_underscore(lineDetail[25].split(']')[1].replace(' ', '-')))
                pokemon.add_item(upper_case_to_underscore(lineDetail[27]))
                pokemon.add_ability(upper_case_to_underscore(lineDetail[28]))
                pokemon.add_teratype(lineDetail[36].split(']')[0].split(',')[-1].replace('\n', ''))
                pokemon.add_move(upper_case_to_underscore(lineDetail[29].split(',')[0]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[29].split(',')[1]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[29].split(',')[2]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[29].split(',')[3]))
                all_pokemons1.append(pokemon)

                pokemon = Pokemon()
                pokemon.add_name(upper_case_to_underscore(lineDetail[36].split(']')[1].replace(' ', '-')))
                pokemon.add_item(upper_case_to_underscore(lineDetail[38]))
                pokemon.add_ability(upper_case_to_underscore(lineDetail[39]))
                pokemon.add_teratype(lineDetail[47].split(']')[0].split(',')[-1].replace('\n', ''))
                pokemon.add_move(upper_case_to_underscore(lineDetail[40].split(',')[0]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[40].split(',')[1]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[40].split(',')[2]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[40].split(',')[3]))
                all_pokemons1.append(pokemon)

                pokemon = Pokemon()
                pokemon.add_name(upper_case_to_underscore(lineDetail[47].split(']')[1].replace(' ', '-')))
                pokemon.add_item(upper_case_to_underscore(lineDetail[49]))
                pokemon.add_ability(upper_case_to_underscore(lineDetail[50]))
                pokemon.add_teratype(lineDetail[58].split(']')[0].split(',')[-1].replace('\n', ''))
                pokemon.add_move(upper_case_to_underscore(lineDetail[51].split(',')[0]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[51].split(',')[1]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[51].split(',')[2]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[51].split(',')[3]))
                all_pokemons1.append(pokemon)

                pokemon = Pokemon()
                pokemon.add_name(upper_case_to_underscore(lineDetail[58].split(']')[1].replace(' ', '-')))
                pokemon.add_item(upper_case_to_underscore(lineDetail[60]))
                pokemon.add_ability(upper_case_to_underscore(lineDetail[61]))
                pokemon.add_teratype(lineDetail[69].split(']')[0].split(',')[-1].replace('\n', ''))
                pokemon.add_move(upper_case_to_underscore(lineDetail[62].split(',')[0]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[62].split(',')[1]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[62].split(',')[2]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[62].split(',')[3]))
                all_pokemons1.append(pokemon)

            if lineDetail[2] == 'p2':
                pokemon = Pokemon()
                pokemon.add_name(upper_case_to_underscore(lineDetail[3].replace(' ', '-')))
                pokemon.add_item(upper_case_to_underscore(lineDetail[5]))
                pokemon.add_ability(upper_case_to_underscore(lineDetail[6]))
                pokemon.add_teratype(lineDetail[14].split(']')[0].split(',')[-1].replace('\n', ''))
                pokemon.add_move(upper_case_to_underscore(lineDetail[7].split(',')[0]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[7].split(',')[1]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[7].split(',')[2]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[7].split(',')[3]))
                all_pokemons2.append(pokemon)

                pokemon = Pokemon()
                pokemon.add_name(upper_case_to_underscore(lineDetail[14].split(']')[1].replace(' ', '-')))
                pokemon.add_item(upper_case_to_underscore(lineDetail[16]))
                pokemon.add_ability(upper_case_to_underscore(lineDetail[17]))
                pokemon.add_teratype(lineDetail[25].split(']')[0].split(',')[-1].replace('\n', ''))
                pokemon.add_move(upper_case_to_underscore(lineDetail[18].split(',')[0]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[18].split(',')[1]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[18].split(',')[2]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[18].split(',')[3]))
                all_pokemons2.append(pokemon)

                pokemon = Pokemon()
                pokemon.add_name(upper_case_to_underscore(lineDetail[25].split(']')[1].replace(' ', '-')))
                pokemon.add_item(upper_case_to_underscore(lineDetail[27]))
                pokemon.add_ability(upper_case_to_underscore(lineDetail[28]))
                pokemon.add_teratype(lineDetail[36].split(']')[0].split(',')[-1].replace('\n', ''))
                pokemon.add_move(upper_case_to_underscore(lineDetail[29].split(',')[0]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[29].split(',')[1]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[29].split(',')[2]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[29].split(',')[3]))
                all_pokemons2.append(pokemon)

                pokemon = Pokemon()
                pokemon.add_name(upper_case_to_underscore(lineDetail[36].split(']')[1].replace(' ', '-')))
                pokemon.add_item(upper_case_to_underscore(lineDetail[38]))
                pokemon.add_ability(upper_case_to_underscore(lineDetail[39]))
                pokemon.add_teratype(lineDetail[47].split(']')[0].split(',')[-1].replace('\n', ''))
                pokemon.add_move(upper_case_to_underscore(lineDetail[40].split(',')[0]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[40].split(',')[1]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[40].split(',')[2]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[40].split(',')[3]))
                all_pokemons2.append(pokemon)

                pokemon = Pokemon()
                pokemon.add_name(upper_case_to_underscore(lineDetail[47].split(']')[1].replace(' ', '-')))
                pokemon.add_item(upper_case_to_underscore(lineDetail[49]))
                pokemon.add_ability(upper_case_to_underscore(lineDetail[50]))
                pokemon.add_teratype(lineDetail[58].split(']')[0].split(',')[-1].replace('\n', ''))
                pokemon.add_move(upper_case_to_underscore(lineDetail[51].split(',')[0]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[51].split(',')[1]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[51].split(',')[2]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[51].split(',')[3]))
                all_pokemons2.append(pokemon)

                pokemon = Pokemon()
                pokemon.add_name(upper_case_to_underscore(lineDetail[58].split(']')[1].replace(' ', '-')))
                pokemon.add_item(upper_case_to_underscore(lineDetail[60]))
                pokemon.add_ability(upper_case_to_underscore(lineDetail[61]))
                pokemon.add_teratype(lineDetail[69].split(']')[0].split(',')[-1].replace('\n', ''))
                pokemon.add_move(upper_case_to_underscore(lineDetail[62].split(',')[0]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[62].split(',')[1]))
                pokemon.add_move(upper_case_to_underscore(lineDetail[62].split(',')[2]))
                if len(lineDetail[62].split(',')) > 3: pokemon.add_move(
                    upper_case_to_underscore(lineDetail[62].split(',')[3]))
                all_pokemons2.append(pokemon)

    #timeGame = strftime('%Y-%m-%d %H:%M:%S', localtime(int(timeGame)))
    all_info['time'] = timeGame
    all_info['source'] = 'showdown'
    all_info['tier'] = tier
    player1info = dict()
    player1info['name'] = player1
    player1info['pokemons'] = []
    player1info['elo'] = elo1
    player2info = dict()
    player2info['name'] = player2
    player2info['pokemons'] = []
    player2info['elo'] = elo2

    for pokemon in all_pokemons1:
        new_pokemon = dict()
        new_pokemon['name'] = pokemon.name
        new_pokemon['ability'] = pokemon.ability
        new_pokemon['tera'] = pokemon.tera
        new_pokemon['item'] = pokemon.item
        new_pokemon['moves'] = pokemon.moves
        has_played = False
        if pokemon.name in all_pokemon_player_1: has_played = True
        new_pokemon['has_played'] = has_played
        has_started = False
        if first_pokemon_player_1_a == pokemon.name:
            has_started = True
        elif first_pokemon_player_1_b == pokemon.name:
            has_started = True
        new_pokemon['has_started'] = has_started
        player1info['pokemons'].append(new_pokemon)

    for pokemon in all_pokemons2:
        new_pokemon = dict()
        new_pokemon['name'] = pokemon.name
        new_pokemon['ability'] = pokemon.ability
        new_pokemon['tera'] = pokemon.tera
        new_pokemon['item'] = pokemon.item
        new_pokemon['moves'] = pokemon.moves
        has_played = False
        if pokemon.name in all_pokemon_player_2: has_played = True
        new_pokemon['has_played'] = has_played
        has_started = False
        if first_pokemon_player_2_a == pokemon.name:
            has_started = True
        elif first_pokemon_player_2_b == pokemon.name:
            has_started = True
        new_pokemon['has_started'] = has_started
        player2info['pokemons'].append(new_pokemon)

    all_info['winner'] = winner
    all_info['player1'] = player1info
    all_info['player2'] = player2info
    if is_valid:
        return all_info
    return None


def get_pokemon_serialized(pokemon):
    all_moves = '|'.join(sorted(pokemon['moves']))
    final_string = pokemon['name'] + ":" + pokemon['ability'] + ":" + pokemon['tera'] + ":" + pokemon['item'] + ":" + all_moves
    return final_string