# Lab number 8 gui stuff
# code written by Brandan Wood Comp 593 with guidance from Jeremy Dalby
# desc - runs a gui which allows one to obtain info on any pokemon entered into the search bar.
# usage - python lab8.py
# pokeapi.py required for pokemon1 import from pokeapi
# :)

from tkinter import *
from tkinter import ttk
from pokeapi import pokemon1

def main():

# creates the window
    root = Tk()
    root.title("PokeViewer")
    root.iconbitmap("ultraball.ico")

# makes the frames for the window
    frm_user_input = ttk.Frame(root)
    frm_user_input.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    frm_info = ttk.LabelFrame(root, text='Info')
    frm_info.grid(row=1, column=0, padx=10, pady=10)

    frm_stats = ttk.LabelFrame(root, text='Stats')
    frm_stats.grid(row=1, column=1, padx=10, pady=10)

# user input frame :O
    lbl_name = ttk.Label(frm_user_input, text='Pokemon Name:')
    lbl_name.grid(row=0, column=0, padx=20, pady=20)

# entry stuff
    ent_name = ttk.Entry(frm_user_input)
    ent_name.grid(row=0, column=1, padx=0, pady=20)
# button stuff
    def btn_click_info():
        pokemon_name = ent_name.get()
        pokeinfo = pokemon1(pokemon_name)
        if pokeinfo:
            lbl_height_val['text'] = str(pokeinfo['height']) + ' dm'
            lbl_weight_val['text'] = str(pokeinfo['weight']) + ' hg'

            types_list =[t['type']['name'] for t in pokeinfo['types']]

            lbl_type_val['text'] = ', '.join(types_list)
            prg_hp['value'] = pokeinfo['stats'][0]['base_stat']
            prg_attack['value'] = pokeinfo['stats'][1]['base_stat']
            prg_defense['value'] = pokeinfo['stats'][2]['base_stat']
            prg_specattack['value'] = pokeinfo['stats'][3]['base_stat']
            prg_specdefense['value'] = pokeinfo['stats'][4]['base_stat']
            prg_speed['value'] = pokeinfo['stats'][5]['base_stat']

    btn_get_info = ttk.Button(frm_user_input, text='Get Info!', command=btn_click_info)
    btn_get_info.grid(row=0, column=2, padx=20, pady=20)

# populate widgets for info frame
    lbl_height = ttk.Label(frm_info, text='Height:')
    lbl_height.grid(row=100, column=100, padx=10, pady=10)

    lbl_height_val = ttk.Label(frm_info, text='TBD')
    lbl_height_val.grid(row=100, column=200, padx=10, pady=10)

    lbl_weight = ttk.Label(frm_info, text='Weight:')
    lbl_weight.grid(row=200, column=100, padx=10, pady=10)

    lbl_weight_val = ttk.Label(frm_info, text='TBD')
    lbl_weight_val.grid(row=200, column=200, padx=10, pady=10)

    lbl_type = ttk.Label(frm_info, text='Type:')
    lbl_type.grid(row=300, column=100, padx=10, pady=10)

    lbl_type_val = ttk.Label(frm_info, text='TBD')
    lbl_type_val.grid(row=300, column=200, padx=10, pady=10)

# populating the stats frame
    lbl_hp = ttk.Label(frm_stats, text='HP:')
    lbl_hp.grid(row=100, column=100)
    prg_hp = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_hp.grid(row=100, column=200)

    lbl_attack = ttk.Label(frm_stats, text='Attack:')
    lbl_attack.grid(row=200, column=100)
    prg_attack = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_attack.grid(row=200, column=200)


    lbl_defense = ttk.Label(frm_stats, text='Defense:')
    lbl_defense.grid(row=300, column=100)
    prg_defense = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_defense.grid(row=300, column=200)


    lbl_specattack = ttk.Label(frm_stats, text='Special Attack:')
    lbl_specattack.grid(row=400, column=100)
    prg_specattack = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_specattack.grid(row=400, column=200)


    lbl_specdefense = ttk.Label(frm_stats, text='Special Defense:')
    lbl_specdefense.grid(row=500, column=100)
    prg_specdefense = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_specdefense.grid(row=500, column=200)


    lbl_speed = ttk.Label(frm_stats, text='Speed:')
    lbl_speed.grid(row=600, column=100)
    prg_speed = ttk.Progressbar(frm_stats, length=200, maximum=255)
    prg_speed.grid(row=600, column=200)

    root.mainloop()


main()

