import streamlit as st
from utils.utilities import set_logos, get_pokemon_type_image_url
from utils.pokemon_showdown_parser import parse_showdown_game, get_pokemon_serialized
from io import StringIO
import pandas as pd

st.set_page_config(layout="wide")
set_logos()
st.title("Professor Wilreg's Laboratory")

all_files = st.file_uploader(label="Upload Showdown Games", key="fileUploader", accept_multiple_files=True)
all_players = []

def get_pokemon_image_name(pokemon):
    pokemon_name = pokemon.lower().replace('indeedee-f', 'indeedee-female').replace('-alola', '-alolan').replace('-rapid-strike', '').replace('-single-strike', '').replace('-hisui', '-hisuian').replace('-masterpiece','').replace('-galar','-galarian')
    return '<img src=https://img.pokemondb.net/sprites/scarlet-violet/normal/'+pokemon_name+'.png alt="'+pokemon_name+'" height=45>'

if not all_files: st.stop()
data = []
for x in all_files:
    new_data = parse_showdown_game(StringIO(x.getvalue().decode("utf-8")).readlines())
    if new_data is None: continue
    data.append(new_data)
    if new_data['player1']['name'] not in all_players: all_players.append(new_data['player1']['name'])
    if new_data['player2']['name'] not in all_players: all_players.append(new_data['player2']['name'])

my_trainers = st.multiselect(label="Select your Trainer Names", options=all_players)
if not my_trainers: st.stop()
col1, col2, col3, col4, col5 = st.columns([1,2,2,1,1])
all_trainers_1 = []
all_trainers_2 = []
pokemon_1_1 = []
pokemon_1_2 = []
pokemon_1_3 = []
pokemon_1_4 = []
pokemon_1_5 = []
pokemon_1_6 = []
pokemon_2_1 = []
pokemon_2_2 = []
pokemon_2_3 = []
pokemon_2_4 = []
pokemon_2_5 = []
pokemon_2_6 = []
result = []
empty = []
num_total_wins = 0
num_total_looses = 0

# Statistics
all_leads_info_win = dict() #(pokemon_1, pokemon_2): num
all_leads_info_loose = dict() #(pokemon_1, pokemon_2): num

all_pokemon_oponent_win = dict() #pokemon: num
all_pokemon_oponent_loose = dict() #pokemon: num

all_pokemons_from_opponent = dict() #pokemon-all-info:ocurrences

#TODO: a desarrollar
pokemons_from_oponent = dict()

all_games_processed = []
for game in data:
    if game['player1']['name'] not in my_trainers and game['player2']['name'] not in my_trainers: continue
    all_games_processed.append(game)
    empty.append("-")
    all_trainers_1.append(game['player1']['name'])
    all_trainers_2.append(game['player2']['name'])
    all_pokemon_images_1 = ''
    all_pokemon_images_2 = ''
    if game['winner'] in my_trainers:
        result.append('WIN')
        num_total_wins += 1
    else:
        result.append('LOOSE')
        num_total_looses += 1

    pokemon_1_1.append(get_pokemon_image_name(game['player1']['pokemons'][0]['name']))
    pokemon_1_2.append(get_pokemon_image_name(game['player1']['pokemons'][1]['name']))
    pokemon_1_3.append(get_pokemon_image_name(game['player1']['pokemons'][2]['name']))
    pokemon_1_4.append(get_pokemon_image_name(game['player1']['pokemons'][3]['name']))
    pokemon_1_5.append(get_pokemon_image_name(game['player1']['pokemons'][4]['name']))
    pokemon_1_6.append(get_pokemon_image_name(game['player1']['pokemons'][5]['name']))

    pokemon_2_1.append(get_pokemon_image_name(game['player2']['pokemons'][0]['name']))
    pokemon_2_2.append(get_pokemon_image_name(game['player2']['pokemons'][1]['name']))
    pokemon_2_3.append(get_pokemon_image_name(game['player2']['pokemons'][2]['name']))
    pokemon_2_4.append(get_pokemon_image_name(game['player2']['pokemons'][3]['name']))
    pokemon_2_5.append(get_pokemon_image_name(game['player2']['pokemons'][4]['name']))
    pokemon_2_6.append(get_pokemon_image_name(game['player2']['pokemons'][5]['name']))

    # Get stats for Leads
    if game['player1']['name'] in my_trainers:
        pokemons_in_lead_win = []
        pokemons_in_lead_loose = []
        for pokemon in game['player1']['pokemons']:
            if game['winner'] in my_trainers and pokemon['has_started']: pokemons_in_lead_win.append(pokemon['name'])
            if game['winner'] not in my_trainers and pokemon['has_started']: pokemons_in_lead_loose.append(pokemon['name'])
        pokemons_in_lead_win.sort()
        pokemons_in_lead_loose.sort()
        if len(pokemons_in_lead_win)==2:
            if (pokemons_in_lead_win[0],pokemons_in_lead_win[1]) not in all_leads_info_win:
                all_leads_info_win[(pokemons_in_lead_win[0],pokemons_in_lead_win[1])] = 1
            else:
                all_leads_info_win[(pokemons_in_lead_win[0], pokemons_in_lead_win[1])] += 1
        if len(pokemons_in_lead_loose)==2:
            if (pokemons_in_lead_loose[0],pokemons_in_lead_loose[1]) not in all_leads_info_loose:
                all_leads_info_loose[(pokemons_in_lead_loose[0],pokemons_in_lead_loose[1])] = 1
            else:
                all_leads_info_loose[(pokemons_in_lead_loose[0], pokemons_in_lead_loose[1])] += 1

    # Get stats for Leads
    if game['player2']['name'] in my_trainers:
        pokemons_in_lead_win = []
        pokemons_in_lead_loose = []
        for pokemon in game['player2']['pokemons']:
            if game['winner'] in my_trainers and pokemon['has_started']: pokemons_in_lead_win.append(
                pokemon['name'])
            if game['winner'] not in my_trainers and pokemon['has_started']: pokemons_in_lead_loose.append(
                pokemon['name'])
        pokemons_in_lead_win.sort()
        pokemons_in_lead_loose.sort()
        if len(pokemons_in_lead_win) == 2:
            if (pokemons_in_lead_win[0], pokemons_in_lead_win[1]) not in all_leads_info_win:
                all_leads_info_win[(pokemons_in_lead_win[0], pokemons_in_lead_win[1])] = 1
            else:
                all_leads_info_win[(pokemons_in_lead_win[0], pokemons_in_lead_win[1])] += 1
        if len(pokemons_in_lead_loose) == 2:
            if (pokemons_in_lead_loose[0], pokemons_in_lead_loose[1]) not in all_leads_info_loose:
                all_leads_info_loose[(pokemons_in_lead_loose[0], pokemons_in_lead_loose[1])] = 1
            else:
                all_leads_info_loose[(pokemons_in_lead_loose[0], pokemons_in_lead_loose[1])] += 1

    # Get stats for oponents pokemon
    if game['player1']['name'] not in my_trainers:
        for pokemon in game['player1']['pokemons']:
            if get_pokemon_serialized(pokemon) not in all_pokemons_from_opponent:
                all_pokemons_from_opponent[get_pokemon_serialized(pokemon)] = 0
            all_pokemons_from_opponent[get_pokemon_serialized(pokemon)] += 1
            if not pokemon['has_played']: continue
            if game['winner'] == game['player1']['name']:
                if pokemon['name'] not in all_pokemon_oponent_loose:
                    all_pokemon_oponent_loose[pokemon['name']] = 0
                all_pokemon_oponent_loose[pokemon['name']] += 1
            else:
                if pokemon['name'] not in all_pokemon_oponent_win:
                    all_pokemon_oponent_win[pokemon['name']] = 0
                all_pokemon_oponent_win[pokemon['name']] += 1

    if game['player2']['name'] not in my_trainers:
        for pokemon in game['player2']['pokemons']:
            if get_pokemon_serialized(pokemon) not in all_pokemons_from_opponent:
                all_pokemons_from_opponent[get_pokemon_serialized(pokemon)] = 0
            all_pokemons_from_opponent[get_pokemon_serialized(pokemon)] += 1
            if not pokemon['has_played']: continue
            if game['winner'] == game['player2']['name']:
                if pokemon['name'] not in all_pokemon_oponent_loose:
                    all_pokemon_oponent_loose[pokemon['name']] = 0
                all_pokemon_oponent_loose[pokemon['name']] += 1
            else:
                if pokemon['name'] not in all_pokemon_oponent_win:
                    all_pokemon_oponent_win[pokemon['name']] = 0
                all_pokemon_oponent_win[pokemon['name']] += 1



df = pd.DataFrame({'Result': result,
                    'Trainer 1': all_trainers_1,
                   'Pokemon 1 Data': pokemon_1_1,
                   'Pokemon 2 Data': pokemon_1_2,
                   'Pokemon 3 Data': pokemon_1_3,
                   'Pokemon 4 Data': pokemon_1_4,
                   'Pokemon 5 Data': pokemon_1_5,
                   'Pokemon 6 Data': pokemon_1_6,
                   ' VS ': empty,
                   'Pokemon 7 Data': pokemon_2_1,
                   'Pokemon 8 Data': pokemon_2_2,
                   'Pokemon 9 Data': pokemon_2_3,
                   'Pokemon 10 Data': pokemon_2_4,
                   'Pokemon 11 Data': pokemon_2_5,
                   'Pokemon 12 Data': pokemon_2_6,
                   'Trainer 2': all_trainers_2
                    })

def highlight(col):
    ans = []
    for col_details in col:
        c = "#D3ECB4" if col_details == 'WIN' else "#ECB4B4"
        ans.append(f"background-color: {c};")
    return ans

def playing_1(col):
    ans = []
    for idx, col_details in enumerate(col):
        all_pokemon_lead = []
        all_pokemon_play = []
        if all_games_processed[idx]['player1']['pokemons'][0]['has_played']: all_pokemon_play.append(get_pokemon_image_name(all_games_processed[idx]['player1']['pokemons'][0]['name']))
        if all_games_processed[idx]['player1']['pokemons'][1]['has_played']: all_pokemon_play.append(get_pokemon_image_name(all_games_processed[idx]['player1']['pokemons'][1]['name']))
        if all_games_processed[idx]['player1']['pokemons'][2]['has_played']: all_pokemon_play.append(get_pokemon_image_name(all_games_processed[idx]['player1']['pokemons'][2]['name']))
        if all_games_processed[idx]['player1']['pokemons'][3]['has_played']: all_pokemon_play.append(get_pokemon_image_name(all_games_processed[idx]['player1']['pokemons'][3]['name']))
        if all_games_processed[idx]['player1']['pokemons'][4]['has_played']: all_pokemon_play.append(get_pokemon_image_name(all_games_processed[idx]['player1']['pokemons'][4]['name']))
        if all_games_processed[idx]['player1']['pokemons'][5]['has_played']: all_pokemon_play.append(get_pokemon_image_name(all_games_processed[idx]['player1']['pokemons'][5]['name']))
        if all_games_processed[idx]['player1']['pokemons'][0]['has_started']: all_pokemon_lead.append(get_pokemon_image_name(all_games_processed[idx]['player1']['pokemons'][0]['name']))
        if all_games_processed[idx]['player1']['pokemons'][1]['has_started']: all_pokemon_lead.append(get_pokemon_image_name(all_games_processed[idx]['player1']['pokemons'][1]['name']))
        if all_games_processed[idx]['player1']['pokemons'][2]['has_started']: all_pokemon_lead.append(get_pokemon_image_name(all_games_processed[idx]['player1']['pokemons'][2]['name']))
        if all_games_processed[idx]['player1']['pokemons'][3]['has_started']: all_pokemon_lead.append(get_pokemon_image_name(all_games_processed[idx]['player1']['pokemons'][3]['name']))
        if all_games_processed[idx]['player1']['pokemons'][4]['has_started']: all_pokemon_lead.append(get_pokemon_image_name(all_games_processed[idx]['player1']['pokemons'][4]['name']))
        if all_games_processed[idx]['player1']['pokemons'][5]['has_started']: all_pokemon_lead.append(get_pokemon_image_name(all_games_processed[idx]['player1']['pokemons'][5]['name']))
        if col_details in all_pokemon_lead:
            ans.append(f"background-color: #DEF3FF;")
        elif col_details in all_pokemon_play:
            ans.append(f"background-color: #C0CDD4;")
        else:
            ans.append(None)
    return ans

def playing(col):
    ans = []
    for c in col:
        ans.append(None)
    return ans

def playing_2(col):
    ans = []
    for idx, col_details in enumerate(col):
        all_pokemon_lead = []
        all_pokemon_play = []
        if all_games_processed[idx]['player2']['pokemons'][0]['has_played']: all_pokemon_play.append(get_pokemon_image_name(all_games_processed[idx]['player2']['pokemons'][0]['name']))
        if all_games_processed[idx]['player2']['pokemons'][1]['has_played']: all_pokemon_play.append(get_pokemon_image_name(all_games_processed[idx]['player2']['pokemons'][1]['name']))
        if all_games_processed[idx]['player2']['pokemons'][2]['has_played']: all_pokemon_play.append(get_pokemon_image_name(all_games_processed[idx]['player2']['pokemons'][2]['name']))
        if all_games_processed[idx]['player2']['pokemons'][3]['has_played']: all_pokemon_play.append(get_pokemon_image_name(all_games_processed[idx]['player2']['pokemons'][3]['name']))
        if all_games_processed[idx]['player2']['pokemons'][4]['has_played']: all_pokemon_play.append(get_pokemon_image_name(all_games_processed[idx]['player2']['pokemons'][4]['name']))
        if all_games_processed[idx]['player2']['pokemons'][5]['has_played']: all_pokemon_play.append(get_pokemon_image_name(all_games_processed[idx]['player2']['pokemons'][5]['name']))
        if all_games_processed[idx]['player2']['pokemons'][0]['has_started']: all_pokemon_lead.append(get_pokemon_image_name(all_games_processed[idx]['player2']['pokemons'][0]['name']))
        if all_games_processed[idx]['player2']['pokemons'][1]['has_started']: all_pokemon_lead.append(get_pokemon_image_name(all_games_processed[idx]['player2']['pokemons'][1]['name']))
        if all_games_processed[idx]['player2']['pokemons'][2]['has_started']: all_pokemon_lead.append(get_pokemon_image_name(all_games_processed[idx]['player2']['pokemons'][2]['name']))
        if all_games_processed[idx]['player2']['pokemons'][3]['has_started']: all_pokemon_lead.append(get_pokemon_image_name(all_games_processed[idx]['player2']['pokemons'][3]['name']))
        if all_games_processed[idx]['player2']['pokemons'][4]['has_started']: all_pokemon_lead.append(get_pokemon_image_name(all_games_processed[idx]['player2']['pokemons'][4]['name']))
        if all_games_processed[idx]['player2']['pokemons'][5]['has_started']: all_pokemon_lead.append(get_pokemon_image_name(all_games_processed[idx]['player2']['pokemons'][5]['name']))
        if col_details in all_pokemon_lead:
            ans.append(f"background-color: #DEF3FF;")
        elif col_details in all_pokemon_play:
            ans.append(f"background-color: #C0CDD4;")
        else:
            ans.append(None)
    return ans

df_styled = df.style.apply(highlight, subset=['Result'])
df_styled = df_styled.apply(playing_1, subset=["Pokemon 1 Data"])
df_styled = df_styled.apply(playing_1, subset=["Pokemon 2 Data"])
df_styled = df_styled.apply(playing_1, subset=["Pokemon 3 Data"])
df_styled = df_styled.apply(playing_1, subset=["Pokemon 4 Data"])
df_styled = df_styled.apply(playing_1, subset=["Pokemon 5 Data"])
df_styled = df_styled.apply(playing_1, subset=["Pokemon 6 Data"])
df_styled = df_styled.apply(playing_2, subset=["Pokemon 7 Data"])
df_styled = df_styled.apply(playing_2, subset=["Pokemon 8 Data"])
df_styled = df_styled.apply(playing_2, subset=["Pokemon 9 Data"])
df_styled = df_styled.apply(playing_2, subset=["Pokemon 10 Data"])
df_styled = df_styled.apply(playing_2, subset=["Pokemon 11 Data"])
df_styled = df_styled.apply(playing_2, subset=["Pokemon 12 Data"])
df_styled= df_styled.hide(axis='columns').hide()


st.header("Games")
st.text("Total Wins: " + str(num_total_wins) + " (" + str(int(num_total_wins*100/(num_total_looses+num_total_wins))) + "%)")
st.text("Total Looses: " + str(num_total_looses) + " (" + str(int(num_total_looses*100/(num_total_looses+num_total_wins))) + "%)")
st.markdown(df_styled.to_html(), unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
col1, col2 = st.columns(2)

# BEST LEADS
col1.header("Win Leads")
first_pokemon_lead = []
second_pokemon_lead = []
perc_ocurrence = []
perc_win_ocurrence = []
if len(all_leads_info_win) > 0:
    for leadkey, leadvalue in all_leads_info_win.items():
        first_pokemon_lead.append(get_pokemon_image_name(leadkey[0]))
        second_pokemon_lead.append(get_pokemon_image_name(leadkey[1]))
        num_perc = str(int(leadvalue*100 / len(all_games_processed))) + '%'
        num_win_perc = str(int(leadvalue*100/num_total_wins)) + '%'
        perc_ocurrence.append(num_perc)
        perc_win_ocurrence.append(num_win_perc)

    df_best_leads = pd.DataFrame({'Pokemon 1': first_pokemon_lead,
                       'Pokemon 2': second_pokemon_lead,
                       'All Games': perc_ocurrence,
                       'Win Games': perc_win_ocurrence,
                       })

    df_best_leads_styled = df_best_leads.style.apply(playing, subset=["Pokemon 1"])
    df_best_leads_styled = df_best_leads_styled.apply(playing, subset=["Pokemon 2"])
    df_best_leads_styled = df_best_leads_styled.hide()
    col1.text("All Games: Percentage of wins of the total games loaded")
    col1.text("Win Games: Percentage of wins of the loaded won games")
    col1.markdown(df_best_leads_styled.to_html(), unsafe_allow_html=True)
else:
    col1.write("There is no data")

# WORST LEADS
col2.header("Loose Leads")
first_pokemon_lead = []
second_pokemon_lead = []
perc_ocurrence = []
perc_win_ocurrence = []
if len(all_leads_info_loose) > 0:
    for leadkey, leadvalue in all_leads_info_loose.items():
        first_pokemon_lead.append(get_pokemon_image_name(leadkey[0]))
        second_pokemon_lead.append(get_pokemon_image_name(leadkey[1]))
        num_perc = str(int(leadvalue * 100 / len(all_games_processed))) + '%'
        num_win_perc = str(int(leadvalue * 100 / num_total_looses)) + '%'
        perc_ocurrence.append(num_perc)
        perc_win_ocurrence.append(num_win_perc)

    df_best_leads = pd.DataFrame({'Pokemon 1': first_pokemon_lead,
                                  'Pokemon 2': second_pokemon_lead,
                                  'All Games': perc_ocurrence,
                                  'Loose Games': perc_win_ocurrence,
                                  })

    df_best_leads_styled = df_best_leads.style.apply(playing, subset=["Pokemon 1"])
    df_best_leads_styled = df_best_leads_styled.apply(playing, subset=["Pokemon 2"])
    df_best_leads_styled = df_best_leads_styled.hide()
    col2.text("All Games: Percentage of looses of the total games loaded")
    col2.text("Win Games: Percentage of looses of the loaded loosed games")
    col2.markdown(df_best_leads_styled.to_html(), unsafe_allow_html=True)
else:
    col2.write("There is no data")

col1, col2 = st.columns(2)

# Best Matchups
col1.write("")
col1.header("Oponents Pokemon Win")
pokemon_best_mu = []
perc_ocurrence = []
perc_win_ocurrence = []
perc_poke_ocurrence = []
if len(all_pokemon_oponent_win)>0:
    all_pokemon_oponent_win = dict(sorted(all_pokemon_oponent_win.items(), key=lambda x: x[1], reverse=True))
    for leadkey, leadvalue in all_pokemon_oponent_win.items():
        pokemon_best_mu.append(get_pokemon_image_name(leadkey))
        num_perc = str(int(leadvalue * 100 / len(all_games_processed))) + '%'
        num_win_perc = str(int(leadvalue * 100 / num_total_wins)) + '%'
        num_poke_perc = '100%'
        if leadkey in all_pokemon_oponent_loose:
            num_poke_perc = str(int(leadvalue * 100 / (leadvalue+all_pokemon_oponent_loose[leadkey]))) + '%'
        perc_ocurrence.append(num_perc)
        perc_win_ocurrence.append(num_win_perc)
        perc_poke_ocurrence.append(num_poke_perc)

    df_best_leads = pd.DataFrame({'Pokemon': pokemon_best_mu,
                                  'All Games': perc_ocurrence,
                                  'Win Games': perc_win_ocurrence,
                                  'Ocurrence Games': perc_poke_ocurrence,
                                  })

    df_best_leads_styled = df_best_leads.style.apply(playing, subset=["Pokemon"])
    df_best_leads_styled = df_best_leads_styled.hide()
    col1.text("All Games: Percentage of victories against this pokemon on all games")
    col1.text("Win Games: Percentage of victories against this pokemon on won games")
    col1.text("Ocurrence Games: Percentage of victories against this pokemon")
    col1.markdown(df_best_leads_styled.to_html(), unsafe_allow_html=True)
else:
    col1.write("There is no data")

# Worst Matchups
col2.write("")
col2.header("Oponents Pokemon Loose")
pokemon_best_mu = []
perc_ocurrence = []
perc_win_ocurrence = []
perc_poke_ocurrence = []
if len(all_pokemon_oponent_loose) > 0:
    all_pokemon_oponent_loose = dict(sorted(all_pokemon_oponent_loose.items(), key=lambda x: x[1], reverse=True))
    for leadkey, leadvalue in all_pokemon_oponent_loose.items():
        pokemon_best_mu.append(get_pokemon_image_name(leadkey))
        num_perc = str(int(leadvalue * 100 / len(all_games_processed))) + '%'
        num_win_perc = str(int(leadvalue * 100 / num_total_looses)) + '%'
        num_poke_perc = '100%'
        if leadkey in all_pokemon_oponent_win:
            num_poke_perc = str(int(leadvalue * 100 / (leadvalue + all_pokemon_oponent_win[leadkey]))) + '%'
        perc_ocurrence.append(num_perc)
        perc_win_ocurrence.append(num_win_perc)
        perc_poke_ocurrence.append(num_poke_perc)

    df_best_leads = pd.DataFrame({'Pokemon': pokemon_best_mu,
                                  'All Games': perc_ocurrence,
                                  'Loose Games': perc_win_ocurrence,
                                  'Ocurrence Games': perc_poke_ocurrence,
                                  })

    df_best_leads_styled = df_best_leads.style.apply(playing, subset=["Pokemon"])
    df_best_leads_styled = df_best_leads_styled.hide()
    col2.text("All Games: Percentage of defeats against this pokemon on all games")
    col2.text("Loose Games: Percentage of defeats against this pokemon on loose games")
    col2.text("Ocurrence Games: Percentage of defeats against this pokemon")
    col2.markdown(df_best_leads_styled.to_html(), unsafe_allow_html=True)
else:
    col2.write("There is no data")

# Pokemon Builds
st.write("")
st.header("Opponents Pokemon Builds")
all_pokemons_names_played_by_oponents = []
for leadkey, leadvalue in all_pokemons_from_opponent.items():
    info_pokemon = leadkey.split(':')
    if info_pokemon[0] not in all_pokemons_names_played_by_oponents:
        all_pokemons_names_played_by_oponents.append(info_pokemon[0])
pokemon_selected = st.selectbox(label="Select a Pokemon from your opponents", options=all_pokemons_names_played_by_oponents)
if not pokemon_selected: st.stop()
pokemon_build = []
pokemon_item = []
pokemon_ability = []
pokemon_tera = []
pokemon_moves = []
pokemon_ocurrences = []
if len(all_pokemons_from_opponent) > 0:
    for leadkey, leadvalue in all_pokemons_from_opponent.items():
        info_pokemon = leadkey.split(':')
        if pokemon_selected != info_pokemon[0]: continue
        pokemon_build.append(get_pokemon_image_name(info_pokemon[0]))
        pokemon_ability.append(info_pokemon[1])
        pokemon_item.append(info_pokemon[3])
        pokemon_tera.append("<img src="+get_pokemon_type_image_url(info_pokemon[2])+" height=25>")
        pokemon_moves.append(info_pokemon[4])
        pokemon_ocurrences.append(leadvalue)

    df_best_leads = pd.DataFrame({'Pokemon': pokemon_build,
                                  'Ability': pokemon_ability,
                                  'Tera': pokemon_tera,
                                  'Item': pokemon_item,
                                  'Moves': pokemon_moves,
                                  'Ocurrences': pokemon_ocurrences,
                                  })

    df_best_leads_styled = df_best_leads.style.apply(playing, subset=["Pokemon"])
    df_best_leads_styled = df_best_leads_styled.apply(playing, subset=["Tera"])
    df_best_leads_styled = df_best_leads_styled.hide()

    st.markdown(df_best_leads_styled.to_html(), unsafe_allow_html=True)
else:
    st.write("There is no data")











