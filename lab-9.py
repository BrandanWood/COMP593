# web api receiving image for tkinter gui.
# python lab-9.py
# written by Brandan Wood COMP 593
# with help from Jeremy Dalby
# :)

import requests
from tkinter import *
from tkinter import ttk
from pokeapi import get_pokemon_image_url
from pokeapi import get_pokemon_list
import ctypes
import os


# main function make window, very good :)
def main():

    script_dir = sys.path[0]

    images_dir = os.path.join(script_dir, 'images')
    if not os.path.isdir(images_dir):
        os.makedirs(images_dir)

    # making the window witha nice little title and sizing the window so it looks nice
    root = Tk()
    root.title("Image PokeViewer")
    root.configure(bg='purple')
    text_font = ('Comic Sans MS', '12')

    # makes it look like a 'real app' with icon in taskbar.
    app_id = 'COMP593.ImagePokeViewer'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    root.iconbitmap(os.path.join(script_dir, "ultraball.ico"))

    # configure the root so it actually centers in the grid
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    frm = ttk.Frame(root)
    frm.grid()

    # image lbl and image setting for the label
    img_pokemon = PhotoImage(file=os.path.join(script_dir, 'pokeball.png'))
    lbl_image = Label(frm, image=img_pokemon, bg='pink')
    lbl_image.grid(row=0, column=0, padx=20, pady=20)
    lbl_image.grid_rowconfigure(0, weight=1)
    lbl_image.grid_columnconfigure(0, weight=1)

    # importing pokeapi to get function for list of pokemon, combo box stuff.
    pokemon_list = get_pokemon_list(limit=1000)
    pokemon_list.sort()

    slct_box = ttk.Combobox(frm, values=pokemon_list, state='readonly', font=text_font)
    slct_box.set('Select a pokemon!')
    slct_box.grid(row=1, column=0)

    def handle_slct_box_pkmn(event):
        """
        get's image based on combo box selection
        params: event for the combo box
        returns: nothing
        """
        pokemon_name = slct_box.get()
        image_url = get_pokemon_image_url(pokemon_name)
        image_path = os.path.join(images_dir, pokemon_name + '.png')
        if get_pkmn_image(image_url, image_path):
            btn_set_desktop.state(['!disabled'])
            img_pokemon['file'] = image_path

    slct_box.bind('<<ComboboxSelected>>', handle_slct_box_pkmn)


    btn_set_desktop = ttk.Button(frm, text='Set as Desktop Image!')
    btn_set_desktop.state(['disabled'])
    btn_set_desktop.grid(row=3, column=0, padx=20, pady=20)

    def get_pkmn_image(url, path):
        """
        :param url: url of the image
        :param path: path where the image is going to be saved
        :return: path where the image is saved
        """

        if os.path.isfile(path):
            return path

        resp_msg = requests.get(url)
        if resp_msg.status_code == 200:
            try:
                image_data = resp_msg.content
                with open(path, 'wb') as fp:
                    fp.write(image_data)
                return path
            except:
                print("didn't work properly. oops!")
                print("here's why?", resp_msg.status_code)
                print(resp_msg.text)
                return
        else:
            print("didn't work properly. oops!")
            print("here's why?", resp_msg.status_code)
            print(resp_msg.text)

    def button_set_desktop_click():
        """
         for setting the desktop on button click
         """
        pokemon_name = slct_box.get()
        path = os.path.join(images_dir, pokemon_name + '.png')
        set_desktop(path)


    def set_desktop(path):
        """
        function that actually sets the desktop background
        :param path: path of image file
        :return: nothing
        """
        try:
            ctypes.windll.user32.SystemParametersInfo(20,0, path, 0)
        except:
            print('problem setting desktop background!')

    root.mainloop()



main()

