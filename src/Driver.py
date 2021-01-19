from tkinter import *
from tkinter.ttk import *
from os import path, getcwd
from src import Player
from src.crops import Apple, Beet, Carrot, Grape, Pineapple, Potato, Rutabaga, Watermelon


def create_new_game():
    global game_objects
    game_objects = [Player.Player("", create_new=True), Apple.Apple("", create_new=True),
                    Beet.Beet("", create_new=True),
                    Carrot.Carrot("", create_new=True), Grape.Grape("", create_new=True),
                    Pineapple.Pineapple("", create_new=True), Potato.Potato("", create_new=True),
                    Rutabaga.Rutabaga("", create_new=True), Watermelon.Watermelon("", create_new=True)]
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


def save_game():
    global game_objects
    save_state = ""
    for obj in game_objects:
        save_state = save_state + obj.save_state() + "\n"
    with open(path.join(getcwd(), '..', 'txt-files', 'load_state'), 'w') as file:
        file.write(save_state)
    display_title_frame()


def display_game_frame():
    global window
    for widget in window.winfo_children():
        widget.destroy()

    game_frame = Frame(window).pack()
    return_to_menu_button = Button(game_frame, text="return to menu",
                                   command=lambda: save_game()).pack()


def load_game():
    global game_objects
    with open(path.join(getcwd(), '..', 'txt-files', 'load_state'), 'r') as file:
        data = file.read().split('\n')
        game_objects = [Player.Player(data[0]), Apple.Apple(data[1]), Beet.Beet(data[2]), Carrot.Carrot(data[3]),
                        Grape.Grape(data[4]), Pineapple.Pineapple(data[5]), Potato.Potato(data[6]),
                        Rutabaga.Rutabaga(data[7]), Watermelon.Watermelon(data[8])]
    display_game_frame()


window = Tk()
window.title("idle eco game")
window.geometry("800x800")
game_objects = []
create_new_game()
display_title_frame()
window.mainloop()
