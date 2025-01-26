import tkinter
import threading
import pyautogui
import time
import keyboard
from pynput import mouse
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# TODO
# - Gerar tempo baseado em 3 grupos
# - Gerar delay entre clicks
# - Implementar variação pequenas de posição

class BrowserManager:

    def __init__(self):
        self.drivers = []

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
        print(window_width)
        window_height = screen_height
        print(window_height)

        thread1 = threading.Thread(target=self.setup_driver, args=(tiktok_url, 0, window_width, window_height))
        thread2 = threading.Thread(target=self.setup_driver, args=(kwai_url, window_width, window_width, window_height))
        thread3 = threading.Thread(target=self.setup_driver, args=(youtube_shorts_url, window_width * 2, window_width, window_height))

        # Inicia as threads
        thread1.start()
        thread2.start()
        thread3.start()

        # Aguarda todas as threads terminarem
        # thread1.join()
        # thread2.join()
        # thread3.join()


    def setup_driver(self,url, position_x, window_width, window_height):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        print(window_width, window_height)
        driver.set_window_size(640, 1000)
        driver.set_window_position(position_x, 0)
        self.drivers.append(driver)

    def close_driver(self, driver):
        try:
            driver.quit()
            print(f"Janela fechada com sucesso!")
        except Exception as e:
            print(f"Erro ao fechar janela: {e}")

    def close_all(self):

        for driver in self.drivers:
            thread = threading.Thread(target=self.close_driver, args=(driver,))
            thread.start()

        self.drivers.clear()


class ClickManager:
    def __init__(self):
        self.click_positions = []
        self.is_recording = False
        self.listener = None
        self.is_clicking = False

    def on_click(self, x, y, button, pressed):
        if pressed and self.is_recording and len(self.click_positions) < 3:
            self.click_positions.append((x, y))
            print(f"Posição {len(self.click_positions)} salva: {x}, {y}")

            if len(self.click_positions) == 3:
                self.stop_recording()
                return False

    def record_clicks(self):
        print("Gravando próximos 3 clicks... Pressione ESC para cancelar.")
        self.click_positions = []
        self.is_recording = True

        with mouse.Listener(on_click=self.on_click) as listener:
            self.listener = listener
            listener.join()

    def stop_recording(self):
        self.is_recording = False
        print("Gravação finalizada!")
        if self.listener:
            self.listener.stop()

    def toggle_clicking(self):
        self.is_clicking = not self.is_clicking
        if self.is_clicking:
            threading.Thread(target=self.click_loop).start()
        print("Auto Clicker:", "Ligado" if self.is_clicking else "Desligado")

    def click_loop(self):
        if not self.click_positions or len(self.click_positions) < 3:
            print("Nenhuma sequência de clicks gravada!")
            self.is_clicking = False
            return

        print("Iniciando sequência de clicks...")
        while self.is_clicking:
            time.sleep(random_delay())
            for pos in self.click_positions:
                if not self.is_clicking:
                    break
                pyautogui.click(pos[0] + random_position(), pos[1] + random_position())

    def start_listener(self):
        keyboard.on_press_key('F8', lambda _: self.toggle_clicking())
        print("Pressione F8 para iniciar/parar a sequência de clicks")

def random_position():
    return random.randint(-4, 4)


def random_delay():
    grupo1_min = 0.5
    grupo1_max = 2

    grupo2_min = 10
    grupo2_max = 25

    grupo3_min = 40
    grupo3_max = 80

    # sortear grupo
    grupo = random.randint(1, 3)

    # selecionar intervalo baseado no grupo
    if grupo == 1:
        delay = random.uniform(grupo1_min, grupo1_max)
    elif grupo == 2:
        delay = random.uniform(grupo2_min, grupo2_max)
    else:
        delay = random.uniform(grupo3_min, grupo3_max)

    return delay

browser_manager = BrowserManager()
click_manager = ClickManager()
click_manager.start_listener()

# Criar janela principal
window = tkinter.Tk()
window.title("Ramos Autoclicker")
window.geometry("500x500")
window.configure(bg='#bdb9b9')

# Criar os botões
button = tkinter.Button(window, text="ABRIR SITES", command=browser_manager.open_sites)
button.pack(side = "top", pady = 25)

button2 = tkinter.Button(window, text="FECHAR NAVEGADOR", command=browser_manager.close_all)
button2.pack(side = "top", pady = 10)

text = tkinter.Label(window, text="Desenvolvido por Salmaze - github.com/KSalmaze")
text.configure(bg='#bdb9b9')
text.pack(side = "bottom")

btn_record = tkinter.Button(window, text="Gravar Clicks", command=click_manager.record_clicks)
btn_record.pack(side="bottom", pady=40)

btn_record = tkinter.Button(window, text="Iniciar Clicks", command=click_manager.toggle_clicking)
btn_record.pack(side="bottom", pady=10)

# Loop principal
window.mainloop()

