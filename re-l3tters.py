import tkinter as tk
from tkinter import ttk
import time
import random

class ASCIIArtGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ASCII Art - Big Letters RE")
        self.window.geometry("1400x900")
        self.window.configure(bg='black')
        
        self.create_widgets()
    
    def create_big_letter_r(self):
        big_r = [
            "RRRRRRRRRRRRRRRRRRRRRRRRRRRR",
            "RRRRRRRRRRRRRRRRRRRRRRRRRRRR",
            "RRRRRRRRRRRRRRRRRRRRRRRRRRRR",
            "RRR                        RRR",
            "RRR                        RRR",
            "RRR                        RRR",
            "RRR                        RRR",
            "RRR                        RRR",
            "RRR                        RRR",
            "RRR                       RRR",
            "RRR                      RRR",
            "RRR                     RRR",
            "RRRRRRRRRRRRRRRRRRRRRRRRR",
            "RRRRRRRRRRRRRRRRRRRRRRRR",
            "RRRRRRRRRRRRRRRRRRRRRRR",
            "RRR                  RRR",
            "RRR                   RRR",
            "RRR                    RRR",
            "RRR                     RRR",
            "RRR                      RRR",
            "RRR                       RRR",
            "RRR                        RRR"
        ]
        return big_r
    
    def create_big_letter_e(self):
        big_e = [
            "EEEEEEEEEEEEEEEEEEEEEEEEEEEE",
            "EEEEEEEEEEEEEEEEEEEEEEEEEEEE",
            "EEEEEEEEEEEEEEEEEEEEEEEEEEEE",
            "EEE                          ",
            "EEE                          ",
            "EEE                          ",
            "EEE                          ",
            "EEE                          ",
            "EEE                          ",
            "EEE                          ",
            "EEE                          ",
            "EEEEEEEEEEEEEEEEEEEEEEEE",
            "EEEEEEEEEEEEEEEEEEEEEEEE",
            "EEEEEEEEEEEEEEEEEEEEEEEE",
            "EEE                          ",
            "EEE                          ",
            "EEE                          ",
            "EEE                          ",
            "EEE                          ",
            "EEE                          ",
            "EEEEEEEEEEEEEEEEEEEEEEEEEEEE",
            "EEEEEEEEEEEEEEEEEEEEEEEEEEEE",
            "EEEEEEEEEEEEEEEEEEEEEEEEEEEE"
        ]
        return big_e
    
    def create_big_letter_r_ascii(self):
        big_r_ascii = [
            "@@@@@@@@####$$$$%%%%&&&&****((()))",
            "@@@@@@@@####$$$$%%%%&&&&****((()))",
            "@@@@@@@@####$$$$%%%%&&&&****((()))",
            "@@@                            @@@",
            "@@@                            @@@",
            "@@@                            @@@",
            "@@@                            @@@",
            "@@@                            @@@",
            "@@@                            @@@",
            "@@@                           @@@",
            "@@@                          @@@",
            "@@@                         @@@",
            "@@@@@@@@####$$$$%%%%&&&&****((",
            "@@@@@@@@####$$$$%%%%&&&&****",
            "@@@@@@@@####$$$$%%%%&&&&**",
            "@@@                  !!!|||",
            "@@@                   //\\\\\\",
            "@@@                    []{}",
            "@@@                     <>?",
            "@@@                      :;",
            "@@@                       _+",
            "@@@                        ~`"
        ]
        return big_r_ascii
    
    def create_big_letter_e_ascii(self):
        big_e_ascii = [
            "!!!!@@@@####$$$$%%%%^^&&****((()))",
            "!!!!@@@@####$$$$%%%%^^&&****((()))",
            "!!!!@@@@####$$$$%%%%^^&&****((()))",
            "!!!                              ",
            "!!!                              ",
            "!!!                              ",
            "!!!                              ",
            "!!!                              ",
            "!!!                              ",
            "!!!                              ",
            "!!!                              ",
            "!!!!@@@@####$$$$%%%%^^&&****",
            "!!!!@@@@####$$$$%%%%^^&&****",
            "!!!!@@@@####$$$$%%%%^^&&****",
            "!!!                              ",
            "!!!                              ",
            "!!!                              ",
            "!!!                              ",
            "!!!                              ",
            "!!!                              ",
            "!!!!@@@@####$$$$%%%%^^&&****((()))",
            "!!!!@@@@####$$$$%%%%^^&&****((()))",
            "!!!!@@@@####$$$$%%%%^^&&****((()))"
        ]
        return big_e_ascii
    
    def create_big_letter_r_matrix(self):
        big_r_matrix = [
            "1111111111111111111111111111",
            "1111111111111111111111111111",
            "1111111111111111111111111111",
            "1110                        111",
            "1110                        111",
            "1110                        111",
            "1110                        111",
            "1110                        111",
            "1110                        111",
            "1110                       111",
            "1110                      111",
            "1110                     111",
            "11111111111111111111111111",
            "1111111111111111111111111",
            "111111111111111111111111",
            "1110                  111",
            "1110                   111",
            "1110                    111",
            "1110                     111",
            "1110                      111",
            "1110                       111",
            "1110                        111"
        ]
        return big_r_matrix
    
    def create_big_letter_e_matrix(self):
        big_e_matrix = [
            "1111111111111111111111111111",
            "1111111111111111111111111111",
            "1111111111111111111111111111",
            "1110                          ",
            "1110                          ",
            "1110                          ",
            "1110                          ",
            "1110                          ",
            "1110                          ",
            "1110                          ",
            "1110                          ",
            "11111111111111111111111111",
            "11111111111111111111111111",
            "11111111111111111111111111",
            "1110                          ",
            "1110                          ",
            "1110                          ",
            "1110                          ",
            "1110                          ",
            "1110                          ",
            "1111111111111111111111111111",
            "1111111111111111111111111111",
            "1111111111111111111111111111"
        ]
        return big_e_matrix
    
    def create_big_letter_r_mixed(self):
        big_r_mixed = [
            "123ABC!@#456DEF$%^789GHI&*(",
            "abcJKL) _+defMNO= []ghiPQR{}",
            "jklSTU| ;:mnoVWX,.<pqrYZ>?/~",
            "ABC                         123",
            "DEF                         456",
            "GHI                         789",
            "JKL                         !@#",
            "MNO                         $%^",
            "PQR                         &*(",
            "STU                        )_+",
            "VWX                       =[]",
            "YZ{                      }|;:",
            "123ABC!@#456DEF$%^789GHI&",
            "abcJKL)_+defMNO=[]ghiPQR",
            "jklSTU|;:mnoVWX,.<pqrYZ",
            "ABC                    >?/~",
            "DEF                     123",
            "GHI                      456",
            "JKL                       789",
            "MNO                        !@#",
            "PQR                         $%^",
            "STU                          &*("
        ]
        return big_r_mixed
    
    def create_big_letter_e_mixed(self):
        big_e_mixed = [
            "QWE123RTY456UIO789PAS!@#DFG",
            "HJK$%^LZX&*(CVB)_+NMQ=[]WER",
            "TYU{}|IO P;:ASD,.<FGH>?/JKL",
            "ZXC                          ",
            "VBN                          ",
            "MQW                          ",
            "ERT                          ",
            "YUI                          ",
            "OPA                          ",
            "SDF                          ",
            "GHJ                          ",
            "KLCVBNMQWERTYUIOPASDFGHJKL",
            "ZXCVBNMQWERTYUIOPASDFGHJKL",
            "ZXCVBNMQWERTYUIOPASDFGHJKL",
            "QWE                          ",
            "RTY                          ",
            "UIO                          ",
            "PAS                          ",
            "DFG                          ",
            "HJK                          ",
            "LZXCVBNMQWERTYUIOPASDFGHJKL",
            "ZXCVBNMQWERTYUIOPASDFGHJKL",
            "ZXCVBNMQWERTYUIOPASDFGHJKL"
        ]
        return big_e_mixed
    
    def create_widgets(self):
        # Заголовок
        title = tk.Label(
            self.window,
            text="ULTRA THICK ASCII LETTERS R E",
            font=("Courier", 26, "bold"),
            fg="#00FF00",
            bg="black"
        )
        title.pack(pady=25)
        
        style_frame = tk.Frame(self.window, bg="black")
        style_frame.pack(pady=20)
        
        tk.Label(style_frame, text="Стиль букв:", font=("Arial", 14, "bold"), 
                fg="white", bg="black").pack(side="left")
        
        self.style_var = tk.StringVar(value="simple")
        style_combo = ttk.Combobox(
            style_frame, 
            textvariable=self.style_var,
            values=["simple", "ascii", "matrix", "mixed"],
            state="readonly",
            width=15
        )
        style_combo.pack(side="left", padx=20)
        style_combo.bind("<<ComboboxSelected>>", self.update_letters)

        self.letters_frame = tk.Frame(self.window, bg="black")
        self.letters_frame.pack(expand=True, pady=30)
        
        self.r_label = tk.Label(
            self.letters_frame,
            font=("Courier", 8, "bold"),
            fg="#00FF00",
            bg="black",
            justify="left"
        )
        self.r_label.pack(side="left", padx=40)
        
        self.e_label = tk.Label(
            self.letters_frame,
            font=("Courier", 8, "bold"),
            fg="#00FF00",
            bg="black",
            justify="left"
        )
        self.e_label.pack(side="left", padx=40)
        
        button_frame = tk.Frame(self.window, bg="black")
        button_frame.pack(pady=25)
        
        self.animate_btn = tk.Button(
            button_frame,
            text="🎬 Запустить анимацию",
            command=self.start_animation,
            font=("Arial", 12),
            bg="#333",
            fg="white",
            width=20
        )
        self.animate_btn.pack(side="left", padx=10)
        
        self.random_btn = tk.Button(
            button_frame,
            text="🎲 Случайные символы",
            command=self.randomize_chars,
            font=("Arial", 12),
            bg="#333", 
            fg="white",
            width=20
        )
        self.random_btn.pack(side="left", padx=10)
        
        self.copy_btn = tk.Button(
            button_frame,
            text="📋 Копировать код",
            command=self.copy_code,
            font=("Arial", 12),
            bg="#333", 
            fg="white",
            width=20
        )
        self.copy_btn.pack(side="left", padx=10)
        
        # Текстовое поле для вывода
        self.output_text = tk.Text(
            self.window,
            height=20,
            width=120,
            font=("Courier", 7),
            bg="black",
            fg="white",
            wrap=tk.NONE
        )
        self.output_text.pack(pady=20, padx=30, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(self.output_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.output_text.yview)
        
        self.update_letters()
    
    def update_letters(self, event=None):
        style = self.style_var.get()
        
        if style == "simple":
            r_art = self.create_big_letter_r()
            e_art = self.create_big_letter_e()
            font_size = 7
        elif style == "ascii":
            r_art = self.create_big_letter_r_ascii()
            e_art = self.create_big_letter_e_ascii()
            font_size = 6
        elif style == "matrix":
            r_art = self.create_big_letter_r_matrix()
            e_art = self.create_big_letter_e_matrix()
            font_size = 6
        else:  # mixed
            r_art = self.create_big_letter_r_mixed()
            e_art = self.create_big_letter_e_mixed()
            font_size = 5
        
        self.r_label.config(text="\n".join(r_art), font=("Courier", font_size, "bold"))
        self.e_label.config(text="\n".join(e_art), font=("Courier", font_size, "bold"))
        self.update_output()
    
    def generate_random_chars(self, pattern):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~"
        result = []
        
        for line in pattern:
            new_line = ""
            for char in line:
                if char == " ":  # Сохраняем пробелы
                    new_line += " "
                else:
                    new_line += random.choice(chars)
            result.append(new_line)
        
        return result
    
    def randomize_chars(self):
        style = self.style_var.get()
        
        if style == "simple":
            r_pattern = self.create_big_letter_r()
            e_pattern = self.create_big_letter_e()
        elif style == "ascii":
            r_pattern = self.create_big_letter_r_ascii()
            e_pattern = self.create_big_letter_e_ascii()
        elif style == "matrix":
            r_pattern = self.create_big_letter_r_matrix()
            e_pattern = self.create_big_letter_e_matrix()
        else:
            r_pattern = self.create_big_letter_r_mixed()
            e_pattern = self.create_big_letter_e_mixed()
        
        new_r = self.generate_random_chars(r_pattern)
        new_e = self.generate_random_chars(e_pattern)
        
        self.r_label.config(text="\n".join(new_r))
        self.e_label.config(text="\n".join(new_e))
        self.update_output_custom(new_r, new_e)
    
    def update_output(self):
        if hasattr(self, 'output_text'):
            self.output_text.delete(1.0, tk.END)
            
            style = self.style_var.get()
            if style == "simple":
                r_art = self.create_big_letter_r()
                e_art = self.create_big_letter_e()
            elif style == "ascii":
                r_art = self.create_big_letter_r_ascii()
                e_art = self.create_big_letter_e_ascii()
            elif style == "matrix":
                r_art = self.create_big_letter_r_matrix()
                e_art = self.create_big_letter_e_matrix()
            else:
                r_art = self.create_big_letter_r_mixed()
                e_art = self.create_big_letter_e_mixed()
            
            self.output_text.insert(tk.END, "🔗 СУПЕР ТОЛСТЫЕ БУКВЫ R и E - ASCII Art (3 символа толщиной):\n")
            self.output_text.insert(tk.END, "="*80 + "\n\n")
            self.output_text.insert(tk.END, "БУКВА R:\n" + "\n".join(r_art) + "\n\n")
            self.output_text.insert(tk.END, "БУКВА E:\n" + "\n".join(e_art))
    
    def update_output_custom(self, r_art, e_art):
        if hasattr(self, 'output_text'):
            self.output_text.delete(1.0, tk.END)
            
            self.output_text.insert(tk.END, "🔗 СУПЕР ТОЛСТЫЕ БУКВЫ R и E - Случайные символы (3 символа толщиной):\n")
            self.output_text.insert(tk.END, "="*80 + "\n\n")
            self.output_text.insert(tk.END, "БУКВА R:\n" + "\n".join(r_art) + "\n\n")
            self.output_text.insert(tk.END, "БУКВА E:\n" + "\n".join(e_art))
    
    def copy_code(self):
        if hasattr(self, 'output_text'):
            code = self.output_text.get(1.0, tk.END)
            self.window.clipboard_clear()
            self.window.clipboard_append(code)
            
            self.copy_btn.config(text="✅ Скопировано!")
            self.window.after(2000, lambda: self.copy_btn.config(text="📋 Копировать код"))
    
    def start_animation(self):
        colors = ["#00FF00", "#00FFFF", "#FF00FF", "#FFFF00", "#FF4444", "#4444FF", "#00FF00"]
        original_text = "🎬 Запустить анимацию"
        self.animate_btn.config(text="⏳ Анимация...", state="disabled")
        
        for color in colors:
            self.r_label.config(fg=color)
            self.e_label.config(fg=color)
            self.window.update()
            time.sleep(0.3)
        
        self.r_label.config(fg="#00FF00")
        self.e_label.config(fg="#00FF00")
        self.animate_btn.config(text=original_text, state="normal")
    
    def run(self):
        self.window.mainloop()

# Запуск программы
if __name__ == "__main__":
    app = ASCIIArtGenerator()

    app.run()
