from selenium import webdriver
import tkinter
from selenium.webdriver.chrome.options import Options

# TODO
# - Paralelizar a abertura de janelas

def open_sites():

    # links
    tiktok_url = "https://www.tiktok.com"
    kwai_url = "https://www.kwai.com"
    youtube_shorts_url = "https://www.youtube.com/shorts"

    # Resolução da tela
    root = tkinter.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()

    # Dimensões das janelas
    window_width = screen_width // 3
    window_height = screen_height

    # Cria as janelas
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s --new-window"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver1 = webdriver.Chrome(options=chrome_options)
    driver2 = webdriver.Chrome(options=chrome_options)
    driver3 = webdriver.Chrome(options=chrome_options)

    # Abre os links
    driver1.get(tiktok_url)
    driver2.get(kwai_url)
    driver3.get(youtube_shorts_url)

    # Configura cada janela
    driver1.set_window_size(window_width, window_height)
    driver1.set_window_position(0, 0)

    driver2.set_window_size(window_width, window_height)
    driver2.set_window_position(window_width, 0)

    driver3.set_window_size(window_width, window_height)
    driver3.set_window_position(window_width * 2, 0)
