import tkinter
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# TODO
# - Paralelizar a abertura de janelas

class BrowserManager:

    def __init__(self):

    def open_sites(self):

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

        thread1 = threading.Thread(target=self.setup_driver, args=(tiktok_url, 0, window_width, window_height))
        thread2 = threading.Thread(target=self.setup_driver, args=(kwai_url, window_width, window_width, window_height))
        thread3 = threading.Thread(target=self.setup_driver, args=(youtube_shorts_url, window_width * 2, window_width, window_height))

        # Inicia as threads
        thread1.start()
        thread2.start()
        thread3.start()

        # Aguarda todas as threads terminarem
        thread1.join()
        thread2.join()
        thread3.join()


    def setup_driver(self,url, position_x, window_width, window_height):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        driver.set_window_size(window_width, window_height)
        driver.set_window_position(position_x, 0)

browser_manager = BrowserManager()

# Criar janela principal
window = tkinter.Tk()
window.title("Ramos Autoclicker")
window.geometry("500x500")
window.configure(bg='#bdb9b9')

# Criar os botões
button = tkinter.Button(window, text="ABRIR SITES", command=browser_manager.open_sites)
button.pack(side = "top", pady = 25)

# Loop principal
window.mainloop()

