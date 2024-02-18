import pathlib
import os
import requests
import shutil
import urllib.request
import re
from bs4 import BeautifulSoup
from mutagen.id3 import ID3, TPE1, TIT2, TDRC, TALB, APIC, ID3NoHeaderError
import customtkinter as ctk

name_of_root_folder = "BYU Speeches"

user_home = pathlib.Path.home()
music_home = os.path.join(user_home, "Music")
root_folder = os.path.join(music_home, name_of_root_folder)
forbiden_characters = [
    '/', 
    '<', 
    '>', 
    ':', 
    '\"', 
    # '\\', 
    '\|', 
    '\?', 
    '\*'
]

replace_string = "$"

BYU_SPEECHES_SPEAKERS_URL = "https://speeches.byu.edu/speakers/"
YEAR_PARSE_REGEX = "(^\d{4}\s|\s\d{4}\s|\s\d{4}$)"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.checkbox_1 = ctk.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = ctk.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.button = ctk.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")



def main():
    
    # print(music_home)
    # holland_talk_obj_lst = get_talk_obj_lst_from_speaker_url("https://speeches.byu.edu/speakers/carlos-e-asay/")
    # download_all_talks_from_obj_lst(holland_talk_obj_lst)

    app = App()
    app.mainloop()

    # download_all_talks_from_all_speakers(BYU_SPEECHES_SPEAKERS_URL)



if __name__ == '__main__':
    main()