from tkinter import *
from chat import get_response, bot_name

# Konstante za boje i fontove
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication:
    def __init__(self):
        self.window = Tk()  # Inicijalizacija glavnog prozora
        self._setup_main_window()  # Postavljanje glavnog prozora

    def run(self):
        self.window.mainloop()  # Pokretanje glavne petlje aplikacije

    def _setup_main_window(self):
        self.window.title("Chat")  # Postavljanje naslova prozora
        # Onemogućavanje promjene veličine prozora
        self.window.resizable(width=False, height=False)
        # Postavljanje dimenzija i boje pozadine prozora
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # Naslovni label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        # Postavljanje širine labela na širinu prozora
        head_label.place(relwidth=1)

        # Linija koja dijeli naslov i sadržaj
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Tekst widget
        self.text_widget = Text(self.window, width=20, height=2,
                                bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scroll bar za tekst widget
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # Label za donji dio prozora
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # Polje za unos poruke
        self.msg_entry = Entry(bottom_label, bg="#2C3E50",
                               fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06,
                             rely=0.008, relx=0.011)
        self.msg_entry.focus()  # Fokus na polje za unos poruke
        # Bindanje Enter tipke na metodu _on_enter_pressed
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Gumb za slanje poruke
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD,
                             width=20, bg=BG_GRAY, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()  # Dohvaćanje teksta iz polja za unos
        self._insert_message(msg, "You")  # Pozivanje metode za umetanje poruke

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)  # Brisanje teksta iz polja za unos
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        # Umjesto END, možete koristiti "end-1c" za ubacivanje ispred kursora
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        # Umjesto END, možete koristiti "end-1c" za ubacivanje ispred kursora
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)  # Automatsko pomicanje na kraj teksta


# Provjera da li je ovo glavni program koji se pokreće
if __name__ == "__main__":
    app = ChatApplication()
    app.run()  # Pokretanje aplikacije
