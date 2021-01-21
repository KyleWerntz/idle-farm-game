from decimal import Decimal
from tkinter import *
from tkinter.ttk import *
from os import path, getcwd
from src import Player
from src.crops import Apple, Beet, Carrot, Grape, Pineapple, Potato, Rutabaga, Watermelon

PLAYER = 0
APPLE = 1
BEET = 2
CARROT = 3
GRAPE = 4
PINEAPPLE = 5
POTATO = 6
RUTABAGA = 7
WATERMELON = 8


def update():
    global game_objects
    for crop in game_objects:
        crop.produce()


def update_display_information():
    global game_objects
    global display_information
    display_information["player_balance"] = StringVar(value=game_objects[PLAYER].get_cash())
    display_information["player_compost"] = StringVar(value=game_objects[PLAYER].get_compost())
    for i in range(1, len(game_objects)):
        crop_name = game_objects[i].get_name() + "_"
        display_information[crop_name + "crops_owned"] = StringVar(value=game_objects[i].get_number_crop_owned())
        display_information[crop_name + "amount_produced"] = StringVar(value=game_objects[i].get_amount_produced())
        display_information[crop_name + "cost_of_next"] = StringVar(value=game_objects[i].get_cost_of_next())
        display_information[crop_name + "potential_sell"] = StringVar(value=game_objects[i].get_potential_sell())
        display_information[crop_name + "potential_compost"] = StringVar(value=game_objects[i].get_potential_compost())


def create_new_game():
    global game_objects
    game_objects = [Player.Player("", create_new=True), Apple.Apple("", create_new=True),
                    Beet.Beet("", create_new=True),
                    Carrot.Carrot("", create_new=True), Grape.Grape("", create_new=True),
                    Pineapple.Pineapple("", create_new=True), Potato.Potato("", create_new=True),
                    Rutabaga.Rutabaga("", create_new=True), Watermelon.Watermelon("", create_new=True)]
    update_display_information()
    display_game_frame()


def load_game():
    global game_objects
    with open(path.join(getcwd(), '..', 'txt-files', 'load_state'), 'r') as file:
        data = file.read().split('\n')
        game_objects = [Player.Player(data[0]), Apple.Apple(data[1]), Beet.Beet(data[2]), Carrot.Carrot(data[3]),
                        Grape.Grape(data[4]), Pineapple.Pineapple(data[5]), Potato.Potato(data[6]),
                        Rutabaga.Rutabaga(data[7]), Watermelon.Watermelon(data[8])]
    update_display_information()
    display_game_frame()


def save_game():
    global game_objects
    save_state = ""
    for obj in game_objects:
        save_state = save_state + obj.save_state() + "\n"
    with open(path.join(getcwd(), '..', 'txt-files', 'load_state'), 'w') as file:
        file.write(save_state)
    display_title_frame()


def display_title_frame():
    global window
    for widget in window.winfo_children():
        widget.destroy()

    title_frame = Frame(window).grid()  # title, new game button, load game button, settings button
    title = Label(title_frame, textvariable="title, image eventually?", anchor=CENTER).grid()
    title_settings_button = Button(title_frame, text="settings").grid()
    title_new_game_button = Button(title_frame, text="new game",
                                   command=lambda: create_new_game()).grid()
    title_load_game_button = Button(title_frame, text="load game",
                                    command=lambda: load_game()).grid()


def display_game_frame():
    global window
    for widget in window.winfo_children():
        widget.destroy()

    game_frame = Frame(window).grid()
    return_to_menu_button = Button(game_frame, text="return to menu",
                                   command=lambda: save_game()).grid()
    player_balance_variable = create_labeled_counter(window, "player balance: ",
                                                     display_information["player_balance"], 2, 0)
    player_compost_variable = create_labeled_counter(window, "player compost: ",
                                                     display_information["player_compost"], 3, 0)
    apple_frame = create_crop_section(window, "Apple", 4, 3)
    beet_frame = create_crop_section(window, "Beet", 4, 10)
    carrot_frame = create_crop_section(window, "Carrot", 10, 3)
    grape_frame = create_crop_section(window, "Grape", 10, 10)
    pineapple_frame = create_crop_section(window, "Pineapple", 16, 3)
    potato_frame = create_crop_section(window, "Potato", 16, 10)
    rutabaga_frame = create_crop_section(window, "Rutabaga", 22, 3)
    watermelon_frame = create_crop_section(window, "Watermelon", 22, 10)


def create_crop_section(master_window, crop_name, row_loc, col_loc):
    new_frame = Frame(master_window).grid()
    name_label = Label(new_frame, text=crop_name).grid(row=row_loc, column=col_loc)
    crops_owned_counter = create_labeled_counter(new_frame, crop_name + "s owned: ",
                                                 display_information[crop_name + "_crops_owned"], row_loc + 1, col_loc)
    amount_produced_counter = create_labeled_counter(new_frame, crop_name + "s produced: ",
                                                     display_information[crop_name + "_amount_produced"], row_loc + 2,
                                                     col_loc)
    cost_of_next_counter = create_labeled_counter(new_frame, crop_name + "'s cost of next: ",
                                                  display_information[crop_name + "_cost_of_next"], row_loc + 3,
                                                  col_loc)
    potential_sell_counter = create_labeled_counter(new_frame, crop_name + "'s potential sell: ",
                                                    display_information[crop_name + "_potential_sell"], row_loc + 4,
                                                    col_loc)
    potential_compost_counter = create_labeled_counter(new_frame, crop_name + "'s potential compost: ",
                                                       display_information[crop_name + "_potential_compost"],
                                                       row_loc + 5, col_loc)
    return new_frame


def create_labeled_counter(master_window, label_message, variable, row_loc, col_loc):
    new_frame = Frame(master_window).grid()
    label = Label(new_frame, text=label_message).grid(row=row_loc, column=col_loc)
    counter = Label(new_frame, textvariable=variable).grid(row=row_loc, column=col_loc + 1)
    return new_frame


window = Tk()
window.title("idle eco game")
window.geometry("800x800")
game_objects = []
display_information = {}
display_title_frame()
window.mainloop()
