import webbrowser
import threading
import tkinter
from selenium import webdriver

def open_urls():
    tiktokUrl = "www.tiktok.com"
    kwaiUrl = "www.kwai.com"
    youtubeShortsUrl = "www.youtube.com/shorts"

    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s --new-window"
    browser = webbrowser.get(chrome_path)

    urls = [tiktokUrl, kwaiUrl, youtubeShortsUrl]
    threads = []

    for url in urls:
        t = threading.Thread(target=open_url, args=(url, browser))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def open_url(url, browser):
    browser.open(url)

def set_resolution_and_position():
    # Obtém resolução da tela
    root = tkinter.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()

    # Calcula dimensões desejadas
    window_width = screen_width // 3
    window_height = screen_height

open_urls()
