import customtkinter as ctk
import forex_python.converter as CurrencyRates
from PIL import Image, ImageTk

from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load('C:/Users/tilak/Documents/Tkinter Apps/currencyapp/Cha Ching- Sound Effects.mp3')


class CurrencyApp(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color= '#272a2e')
        self.title('Currency Converter')
        self.geometry('600x400')
        self.resizable(False, False)
        
        self.frame = ctk.CTkFrame(self, width= 400, height= 200, fg_color= '#29334f')
        self.frame.place(x = 100, y= 70)
        
        self.frame_2 = ctk.CTkFrame(self, width= 300, height= 75)
        self.frame_2.place(x = 150, y= 300)
        
        image = Image.open('C:/Users/tilak/Documents/Tkinter Apps/currencyapp/MONEY.png')
        
        ctk_image = ctk.CTkImage(light_image=image)
        
        label_1 = ctk.CTkLabel(self, text= 'Currency Converter', font= ('Calibri', 30))
        label_1.place(x = 185, y = 20)
        
        n = ['USD', 'EUR', 'GBP', 'INR', 'AUD', 'CAD', 'SGD', 'CHF', 'MYR', 'JPY', 'CNY']
        self.Combobox_var = ctk.StringVar(value="CONVERT FROM")
        Combo_1 = ctk.CTkComboBox(self.frame, width= 150, variable= self.Combobox_var, values= n)
        Combo_1.place(x = 50, y = 15)
        
        self.Combobox_var_2 = ctk.StringVar(value="CONVERT TO")
        Combo_2 = ctk.CTkComboBox(self.frame, width= 150,values= n, variable= self.Combobox_var_2)
        Combo_2.place(x = 200, y = 15)
        
        self.Entry_var = ctk.StringVar(value = [])
        self.Entry_1 = ctk.CTkEntry(self.frame, width= 300, height= 100, placeholder_text= "Enter Amount",textvariable=self.Entry_var,fg_color= '#29334f', bg_color= '#4FBAF0', font= ('Calibri', 50))
        self.Entry_1.place(x = 50, y = 70)
        
        
        
        
        self.button = ctk.CTkButton(self.frame_2, 
                                    image= ctk_image,
                                    compound= 'left', 
                                    text= 'Convert',
                                    height= 50, 
                                    width= 250,
                                    border_width= 0,
                                    command=self.convert_money
                                    )
        self.button.place(x = 25, y = 12.5)
    
    
    
    def convert_money(self):
        from_currency = self.Combobox_var.get()
        to_currency = self.Combobox_var_2.get()
        amount = self.Entry_1.get()
        converted_amount = CurrencyRates.convert(from_currency, to_currency, float(amount))
        self.Entry_var.set(converted_amount)
        mixer.music.play()


__name__ == '__main__'
app = CurrencyApp()
app.mainloop()
    
    