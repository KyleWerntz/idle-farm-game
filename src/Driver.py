from tkinter import *
from tkinter.ttk import *
from os import path, getcwd
from src import Player
from src.crops import Apple, Beet, Carrot, Grape, Pineapple, Potato, Rutabaga, Watermelon

player = ""
apple = ""
beet = ""
carrot = ""
grape = ""
pineapple = ""
potato = ""
rutabaga = ""
watermelon = ""


def create_new_game():
    global player, apple, beet, carrot, grape, pineapple, potato, rutabaga, watermelon
    player = Player.Player("", create_new=True)
    apple = Apple.Apple("", create_new=True)
    beet = Beet.Beet("", create_new=True)
    carrot = Carrot.Carrot("", create_new=True)
    grape = Grape.Grape("", create_new=True)
    pineapple = Pineapple.Pineapple("", create_new=True)
    potato = Potato.Potato("", create_new=True)
    rutabaga = Rutabaga.Rutabaga("", create_new=True)
    watermelon = Watermelon.Watermelon("", create_new=True)
    display_game_frame()


def display_title_frame():
    global window
    for widget in window.winfo_children():
        widget.destroy()

    title_frame = Frame(window).pack()  # title, new game button, load game button, settings button
    title = Label(title_frame, textvariable="title, image eventually?", anchor=CENTER).pack()
    title_settings_button = Button(title_frame, text="settings").pack(expand=True)
    title_new_game_button = Button(title_frame, text="new game",
                                   command=lambda: create_new_game()).pack(side=LEFT, expand=True)
    title_load_game_button = Button(title_frame, text="load game",
                                    command=lambda: load_game()).pack(side=RIGHT, expand=True)  # TODO


def display_game_frame():
    global window
    for widget in window.winfo_children():
        widget.destroy()

    game_frame = Frame(window).pack()
    return_to_menu_button = Button(game_frame, text="return to menu",
                                   command=lambda: display_title_frame()).pack()


def load_game():
    global player, apple, beet, carrot, grape, pineapple, potato, rutabaga, watermelon
    with open(path.join(getcwd(), '..', 'txt-files', 'load_state'), 'r') as file:
        data = file.read().split('\n')
        player = Player.Player(data[0])
        apple = Apple.Apple(data[1])
        beet = Beet.Beet(data[2])
        carrot = Carrot.Carrot(data[3])
        grape = Grape.Grape(data[4])
        pineapple = Pineapple.Pineapple(data[5])
        potato = Potato.Potato(data[6])
        rutabaga = Rutabaga.Rutabaga(data[7])
        watermelon = Watermelon.Watermelon(data[8])
    display_game_frame()


window = Tk()
window.title("idle eco game")
window.geometry("800x800")
display_title_frame()
window.mainloop()
