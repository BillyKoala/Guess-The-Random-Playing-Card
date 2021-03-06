"""
Author: Billy Knight - March 2022.

Project Name: Guess The Random Playing Card.

This is the functions.py file created to
manage the functionality of this project.
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import globals
from globals import *
import constants
import main
from main import *
import threading
import time
import datetime

def close_developer_window(win):
    try:

        win.destroy()

    except Exception as e:
        print(e)

    finally:
        pass

def invert_image(e):

    try:
        image = Image.open(developer_mugshot_inv)
        resize_image = image.resize((230, 280), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        dev_label.config(image=img)
        dev_label.image = img

    except Exception as e:
        print(e)

    finally:
        pass

def revert_image(e):

    try:
        image = Image.open(developer_mugshot)
        resize_image = image.resize((230, 280), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        dev_label.config(image=img)
        dev_label.image = img

    except Exception as e:
        print(e)

    finally:
        pass

def game_developer_window(root):

    try:
        dev_details = "Billy Knight\nPython Developer\nbilly_knight@hotmail.com"
        global dev_label

        # Define the game child window object.
        win = Toplevel(globals.root)
        win.rowconfigure(0, weight=1)
        win.columnconfigure(0, weight=1)
        win.resizable(False, False)

        # Define variables for the window and screen sizes.
        window_width = 450
        window_height = 400
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        """
        Calculate the x and y coordinates for placing
        the parent window in the centre of the screen.
        """
        x_coord = (screen_width / 2) - (window_width / 2)
        y_coord = (screen_height / 2) - (window_height / 2)

        # Place the window in the centre of the screen.
        win.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))

        # Define the look of the game window.
        win.title("Python Game Developer: Billy Knight")
        win.configure(width=window_width, height=window_height, bg="#9e4039")

        # Retrieve the favicon file and attach it to the top left of the window.
        win.iconbitmap("venv/images/fav-icon/favicon.ico")

        dev_frame = Frame(win, width=450, height=400, background="#0352fc",
        highlightbackground="#038cfc", highlightthickness=4)
        dev_frame.place(x=0, y=0)

        dev_label2 = Label(dev_frame, text=dev_details, font=("Arial Black", 10), background="#0352fc")
        dev_label2.place(x=130, y=320)

        image = Image.open(developer_mugshot)
        resize_image = image.resize((230, 280), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        dev_label = Label(dev_frame, image=img, relief="sunken", width=230, height=280)
        dev_label.image = img
        dev_label.place(x=110, y=30)
        dev_label.bind("<Enter>", invert_image)
        dev_label.bind("<Leave>", revert_image)
        btn_close = Button(win, text="OK... That\' Enough!!!", width=14, height=1,
        fg="blue", bg="#34cceb", command=lambda: close_developer_window(win))
        btn_close.place(x=337, y=370)

        win.mainloop()

    except Exception as e:
        print(e)

    finally:
        pass

def generate_random_playing_card(hint_info_label):

    try:
        """
        Instantiate the random playing
        card object and populate it.
        """
        rpc = gen_rand_card(RandomPlayingCard)

        # Show the random playing card for testing.
        print(f"Random Card: {globals.random_card}")

        hint_info_label["text"] = "Getting Cards Ready..."

        thread_insert_playing_card_matrix(hint_info_label)

        # Now update the hint info label.
        hint_info_label["text"] = info_label_dict["before"]#"Select A Playing Card To Get The Game Going"

    except Exception as e:
        print(e)

    finally:
        pass

def sort_into_suits_alphabetically(card_path_array):

    try:
        """
        This function will accept an array argument of 52 card elements, and sort them by
        their suit order (S, D, H, C) and then by their numerical order (Ace - King)
        """
        # Define some variables here.
        suit = ""
        spades = []
        diamonds = []
        hearts = []
        clubs = []
        sorted = []

        for i in range(0, 52):
            suit = card_path_array[i]
            suit = suit[-5]

            if suit == "S":
                spades.append(card_path_array[i])
            elif suit == "D":
                diamonds.append(card_path_array[i])
            elif suit == "H":
                hearts.append(card_path_array[i])
            elif suit == "C":
                clubs.append(card_path_array[i])

        for i in range(len(spades)):
            sorted.append(spades[i])

        for i in range(len(diamonds)):
            sorted.append(diamonds[i])

        for i in range(len(hearts)):
            sorted.append(hearts[i])

        for i in range(len(clubs)):
            sorted.append(clubs[i])

        return sorted

    except Exception as e:
        print(e)

    finally:
        pass

def thread_clear_the_deck(hint_info_label):

    t = threading.Thread(target=clear_the_deck, args=(globals.hint_info_label,)).start()

def clear_the_deck(hint_info_label):

    try:
        # Generate a new random playing card.
        gen_rand_card(RandomPlayingCard)
        show_playing_card(joker_image_path)
        hint_info_label["text"] = info_label_dict.get("before")

        # Remove all the playing cards from the window.
        for card in globals.card_deck:
            time.sleep(0.02)
            card.destroy()

        # Now re-add the playing cards to the window.
        thread_insert_playing_card_matrix(globals.hint_info_label)

        time.sleep(3)

        hint_info_label["text"] = info_label_dict.get("after")

    except Exception as e:
        print(e)

    finally:
        pass

def mouseClick(event):

    try:
        # Increment the attempts count.
        globals.attempt_count += 1

        # Get the name of the button the player clicked on.
        a = event.widget
        button_clicked = a._name[1:]

        # Get the card that was selected by the player.
        selected_card = globals.card_click_dict.get(button_clicked)
        #print(f"Clicked Card: {selected_card}") # Use this code to ensure game recognises clicked card value.

        # Get the card image file path and show the selected card.
        image_path = "venv/images/playingcards/"
        show_playing_card(f"{image_path}{selected_card}.png")

        # Flip card to reverse view.
        image = Image.open(card_reverse_side_image)
        resize_image = image.resize((30, 45), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        a.config(image=img)
        a.image=img

        """
        Now see whether the correct playing card has been selected,
        or if a hint is required to push them in the right direction.
        """
        thread_get_player_hint(selected_card)

    except Exception as e:
        print(e)

    finally:
        pass

def insert_playing_card_matrix(hint_info_label):

    try:
        """
        This function will send 52 playing cards onto the screen.
        """
        card_path = cards_path
        append_card_path = ""
        ext = ".png"
        globals.card_path_array = []
        globals.card_id_array = []
        globals.card_deck = []
        globals.card_click_dict = {}
        card_id = ""
        card_width = 50
        x_axis = 30
        y_axis = 260
        button_name = ""

        for j in range(len(card_number_array)):  # Length = 52
            for i in range(len(card_suit_array)):  # Length = 4
                card_id = card_number_array[j] + card_suit_array[i]  # A + S = Ace Of Spades
                globals.card_id_array.append(card_id)  # Add the card id (AS) to its own array.
                append_card_path = card_path + card_id + ext  # The full path for this card image file.
                globals.card_path_array.append(append_card_path)  # Append this card image file path.

        # Sort the deck by each suit from A - K.
        globals.card_path_array = sort_into_suits_alphabetically(globals.card_path_array)

        for i in range(len(globals.card_path_array)):
            image = Image.open(globals.card_path_array[i])
            resize_image = image.resize((30, 45), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(resize_image)
            card_label = Label(image=img, relief="solid")
            card_label.image = img
            card_id = str(globals.card_path_array[i])
            card_id = card_id.replace(card_path, "").replace(ext, "")

            # Create the playing card button.
            btn_name = Button(globals.root, image=img, text=card_id)
            btn_name.place(x=x_axis, y=y_axis)
            btn_name.bind("<Button-1>", mouseClick)
            card_text = btn_name.cget("text")

            """
            Record the playing cards for removing
            in case the user wants to play again.
            """
            globals.card_deck.append(btn_name)
            button_name = btn_name.winfo_name()
            # Record the button name and playing card.
            globals.card_click_dict[button_name[1:]] = card_text

            time.sleep(0.02)

            if i in range(0, 12):       # First Row (Spades)
                x_axis += card_width
                y_axis = 260
            elif i == 12:
                x_axis = 30
                y_axis = 330
            elif i in range(13, 25):    # Second Row (Diamonds)
                x_axis += card_width
                y_axis = 330
            elif i == 25:
                x_axis = 30
                y_axis = 400
            elif i in range(26, 38):    # Third Row (Hearts)
                x_axis += card_width
                y_axis = 400
            elif i == 38:
                x_axis = 30
                y_axis = 470
            elif i in range(39, 51):    # Fourth Row (Clubs)
                x_axis += card_width
                y_axis = 470

        # Now update the hint info label in the root window.
        hint_info_label["text"] = info_label_dict.get("after")

    except Exception as e:
        print(e)

    finally:
        pass

def thread_insert_playing_card_matrix(hint_info_label):

    try:
        # Run a thread to populate the window with a deck of cards.
        p = threading.Thread(target=insert_playing_card_matrix, args=(hint_info_label,)).start()

    except Exception as e:
        print(e)

    finally:
        pass

def show_card_suits(card_suits_path):

    try:
        # Read the Image.
        image = Image.open(card_suits_path)

        # Resize the image using resize() method.
        resize_image = image.resize((142, 164), Image.ANTIALIAS)

        img = ImageTk.PhotoImage(resize_image)

        # create label add and resize image.
        card_label = Label(image=img, relief="sunken")
        card_label.image = img
        card_label.place(x=529, y=3)

    except Exception as e:
        print(e)

    finally:
        pass

def show_playing_card(card_image_path):

    try:
        # Read the Image
        image = Image.open(card_image_path)

        # Resize the image using resize() method
        resize_image = image.resize((142, 164), Image.ANTIALIAS)

        img = ImageTk.PhotoImage(resize_image)

        # create label add and resize image
        card_label = Label(image=img, relief="solid")
        card_label.image = img
        card_label.place(x=20, y=3)

    except Exception as e:
        print(e)

    finally:
        pass

def thread_get_player_hint(selected_card):

    try:

        h = threading.Thread(target=get_player_hint, args=(selected_card,)).start()

    except Exception as e:
        print(e)

    finally:
        pass

def get_player_hint(selected_card):

    try:
        global player_card_suit_index, random_card_suit_index, player_card_number_index, random_card_number_index
        player_card_suit = selected_card[-1]
        player_card_number = selected_card[0:2] if len(selected_card) == 3 else selected_card[0]
        random_card_suit = globals.card_suit
        random_card_number = globals.card_number
        card_no = card_number_array
        suit_type = card_suit_array
        player_card_number_index = card_number_array.index(player_card_number)
        player_card_suit_index = card_suit_array.index(player_card_suit)
        random_card_number_index = card_number_array.index(random_card_number)
        random_card_suit_index = card_suit_array.index(random_card_suit)

        # Check the selected card number and suit.
        if player_card_suit in card_suit_array:
            if player_card_suit == "S":
                player_card_suit = "Spades"
            if player_card_suit == "D":
                player_card_suit = "Diamonds"
            if player_card_suit == "H":
                player_card_suit = "Hearts"
            if player_card_suit == "C":
                player_card_suit = "Clubs"

        if player_card_number in card_number_array:
            if player_card_number == "A":
                player_card_number = "Ace"
            if player_card_number == "J":
                player_card_number = "Jack"
            if player_card_number == "Q":
                player_card_number = "Queen"
            if player_card_number == "K":
                player_card_number = "King"

        # Check the random card number and suit.
        if random_card_suit in card_suit_array:
            if random_card_suit == "S":
                random_card_suit = "Spades"
            if random_card_suit == "D":
                random_card_suit = "Diamonds"
            if random_card_suit == "H":
                random_card_suit = "Hearts"
            if random_card_suit == "C":
                random_card_suit = "Clubs"

        if random_card_number in card_number_array:
            if random_card_number == "A":
                random_card_number = "Ace"
            if random_card_number == "J":
                random_card_number = "Jack"
            if random_card_number == "Q":
                random_card_number = "Queen"
            if random_card_number == "K":
                random_card_number = "King"

        hint = ""

        """
        Generate a list of hints for the player, or congratulate
        them on selecting the card correctly first time round.
        """
        num_or_pic = "Right Picture Card" if random_card_number in picture_cards_array else "Right Card Number"
        
        hint_list = ["Correct Suit, Go Higher", "Correct Suit, Go Lower ",
                     "Incorrect Suit, Go Higher", "Incorrect Suit, Go Lower",
                     f"{num_or_pic}, Wrong Suit"]

        if player_card_suit_index == random_card_suit_index and player_card_number_index < random_card_number_index:
            hint = hint_list[0]
        elif player_card_suit_index == random_card_suit_index and player_card_number_index > random_card_number_index:
            hint = hint_list[1]
        elif player_card_suit_index != random_card_suit_index and player_card_number_index < random_card_number_index:
            hint = hint_list[2]
        elif player_card_suit_index != random_card_suit_index and player_card_number_index > random_card_number_index:
            hint = hint_list[3]
        elif player_card_suit_index != random_card_suit_index and player_card_number_index == random_card_number_index:
            hint = hint_list[4]
        elif selected_card == globals.random_card: # Player selected the matching playing card.
            if globals.attempt_count == 1: # Did the player guess it right on first attempt?

                globals.hint_info_label["text"] = f"{player_card_number} of {player_card_suit} - " \
                f"Congratulations - You Guessed It Right In ONE Attempt"
                show_random_successful_message()
                time.sleep(3)
                thread_clear_the_deck(globals.hint_info_label)

            else: # No, more than one attempt was made.
                attempts = "Attempt" if globals.attempt_count == 1 else "Attempts"
                globals.hint_info_label["text"] = f"{player_card_number} of {player_card_suit} - " \
                f"Congratulations - You Guessed It Right In {globals.attempt_count} {attempts}"
                time.sleep(3)
                thread_clear_the_deck(globals.hint_info_label)

        # The last attempt was incorrect. Show the selected card as text and offer the player a hint.
        if hint != "": globals.hint_info_label["text"] = f"{player_card_number} of {player_card_suit} - {hint}"

    except Exception as e:
        print(e)

    finally:
        pass

def show_random_successful_message():

    try:
        # Generate a list of congratulatory messages and select one at random.
        rand_messages = ["Well done Champ.\n\nHigh Five!!! ",
                         "Hey, who's your daddy, Luke?.\n\nPop that champagne cork!!!",
                         "Yippee Ki Yay, My Friend.\n\nThe Milky Bars are on you!!!",
                         "Yo, go to the top of the class dude.\n\nIs there any stopping you now?",
                         "OK Genius.\n\nPass Go and collect ??200!!!!",
                         "Get in there you swick dinger you.\n\n\'On Top \'O The World Ma!!!\'"]

        rand_titles = ["Nice One Forest", "Well Howdy Pardner?", "You\'re Smarter Than You Look",
                       "Are You Using The Force?", "No Flies On You, Then?", "You Done This Before?"]

        win_title = f"{random.choice(rand_titles)}"
        win_text = f"{random.choice(rand_messages)}"
        messagebox.showinfo(win_title,win_text)

    except Exception as e:
        print(e)

    finally:
        pass

def gen_rand_card(random_card_object):

    # Reset the attempt count to zero.
    globals.attempt_count = 0

    # Define some variables first.
    card_id = ""
    card_number = ""
    card_suit = ""
    card_suit_name = ""
    card_suit_colour = ""
    card_picture_name = ""
    card_image_path = ""
    globals.attempt_count = 0

    try:
        # Select a random card number and suit.
        card_number = random.choice(card_number_array)
        card_suit = random.choice(card_suit_array)
        card_id = card_number + card_suit
        card_suit_colour = "Black" if (card_suit in ("S", "C")) else "Red"
        card_image_path = card_image_path + card_id + ".png"
        globals.card_image = card_image_path
        globals.card_number = card_number
        globals.random_card = card_id
        globals.card_suit = card_suit

        print(f"GRC: {card_id}")

        # Define the card suit names.
        if card_suit == "S":
            card_suit_name = "Spades"
        elif card_suit == "D":
            card_suit_name = "Diamonds"
        elif card_suit == "H":
            card_suit_name = "Hearts"
        elif card_suit == "C":
            card_suit_name = "Clubs"

        # If the random card is an ace or picture card, then get its name.
        if card_number in card_suit_array:
            if card_number == "A":
                card_picture_name = "Ace"
            elif card_number == "J":
                card_picture_name = "Jack"
            elif card_number == "Q":
                card_picture_name = "Queen"
            elif card_number == "K":
                card_picture_name = "King"
        else:
            card_picture_name = card_number

    except Exception as e:
        print(e)

    finally:
        """
        Instantiate, populate and send the random 
        playing card object back to main.py.
        """
        rpc = random_card_object

        rpc = RandomPlayingCard(card_id,
                                card_number,
                                card_suit,
                                card_suit_name,
                                card_suit_colour,
                                card_picture_name,
                                card_image_path)
    return rpc

def quit_game(root):

    try:
        messagebox_text = "Have You Really Had Enough Of This Game?"

        if messagebox.askyesno("Had Enough?", messagebox_text): root.destroy()

    except Exception as e:
        print(e)

    finally:
        pass
