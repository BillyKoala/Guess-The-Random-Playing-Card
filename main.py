"""
Author: Billy Knight - March 2022.

Project Name: Guess The Random Playing Card.

This is the main.py file created to manage
the look and tkinter widgets of this project.
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import threading
from PIL import Image, ImageTk
from time import *
import globals
import functions
from functions import *
from classes import *

def main():

    info_label_dict = {"before":"Getting Cards Ready...",
                       "after":"Please Select A Playing Card To Get The Game Going",
                       "header":"Welcome To Guess The Random Playing Card"}

    globals.info_label_dict = info_label_dict

    rpc = gen_rand_card(RandomPlayingCard)
    globals.attempt_count = 0
    globals.card_number = rpc.card_number
    globals.card_suit = rpc.card_suit
    globals.random_card = f"{globals.card_number}{globals.card_suit}"
    card_id = rpc.card_id
    suit_name = rpc.suit_name
    suit_colour = rpc.suit_colour
    picture_name = rpc.picture_name
    card_image_path = rpc.card_image_path
    card_suits_image_path = rpc.card_suits_image_path


    # Print the random card for testing purposes.
    print(f"Random Card: {rpc.card_id}")

    try:
        # Define the game parent window object.
        root = tk.Tk()
        globals.root = root
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.resizable(False, False)

        # Define variables for the window and screen sizes.
        window_width = 696
        window_height = 573
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        """
        Calculate the x and y coordinates for placing
        the parent window in the centre of the screen.
        """
        x_coord = (screen_width / 2) - (window_width / 2)
        y_coord = (screen_height / 2) - (window_height / 2)

        # Place the window in the centre of the screen.
        root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))

        # Define the look of the game window.
        root.title("Guess The Random Playing Card")
        root.configure(width=window_width, height=window_height, bg="#5a03fc")

        # Retrieve the favicon file and attach it to the top left of the window.
        root.iconbitmap("venv/images/favicon.ico")

        matrix_frame = Frame(root, width=655, height=356, background="#3256a8",
        highlightbackground="#3275a8", highlightthickness=3)
        matrix_frame.place(x=20, y=175)
        globals.matrix_frame = matrix_frame

        matrix_info_frame = Frame(matrix_frame, width=385, height=60, background="green",
        highlightbackground="#3275a8", highlightthickness=3)
        matrix_info_frame.place(x=7, y=9)
        # Add a welcome banner.
        welcome_info_label = Label(matrix_info_frame, text=info_label_dict.get("header"),
        relief="raised", font=("Arial Black", 11), bg="#1753b3", fg="#b0b317")
        welcome_info_label.pack(padx=125)
        # Add an updatable banner.
        hint_info_label = Label(matrix_info_frame, text=info_label_dict.get("before"),
        fg="#b0b317", relief="raised", font=("Arial Black", 9), bg="#1753b3", width=60)
        hint_info_label.pack(pady=4)
        globals.hint_info_label = hint_info_label
        # Add menus here.
        bk_menu = Menu(root)
        root.config(menu=bk_menu)
        # Options Menu & separated sub options.
        file_menu = Menu(bk_menu)
        bk_menu.add_cascade(label="Options", menu=file_menu)
        file_menu.add_command(label="Play It Again, Sam", command=lambda: thread_clear_the_deck(hint_info_label))
        file_menu.add_separator()
        file_menu.add_command(label="Jeez, I\'ve Had Enough!", command=lambda:quit_game(root))
        # About Menu
        file_menu = Menu(bk_menu)
        bk_menu.add_cascade(label="About", menu=file_menu)
        file_menu.add_command(label="Game Developer", command=lambda: game_developer_window(root))
        # Show the Joker Playing Card (left-hand side).
        show_playing_card(joker_image_path)
        # Show the card suits image (right-hand side).
        show_card_suits(card_suits_image_path)
        # Populate the window with 52 playing cards from left to right.
        thread_insert_playing_card_matrix(hint_info_label)

        root.mainloop()

    except Exception as e:
        print(e)

    finally:
        pass

# Prevent any issues whilst importing modules.
if __name__ == "__main__": main()