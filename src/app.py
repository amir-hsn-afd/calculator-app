import customtkinter as ctk
from calculator import Calculator

# ----------------------------
# |         Configs          |
# ----------------------------
BUTTON_LAYOUT = [
    [
        {'text' : 'C', 'type' : 'clear'},
        {'text' : '⌫', 'type' : 'control'},
        {'text' : '%', 'type' : 'operator'},
        {'text' : '÷', 'type' : 'operator'},
    ],

    [
        {'text' : '7', 'type' : 'number'},
        {'text' : '8', 'type' : 'number'},
        {'text' : '9', 'type' : 'number'},
        {'text' : '×', 'type' : 'operator'},
    ],

    [
        {'text' : '4', 'type' : 'number'},
        {'text' : '5', 'type' : 'number'},
        {'text' : '6', 'type' : 'number'},
        {'text' : '+', 'type' : 'operator'},
    ],

    [
        {'text' : '1', 'type' : 'number'},
        {'text' : '2', 'type' : 'number'},
        {'text' : '3', 'type' : 'number'},
        {'text' : '-', 'type' : 'operator'},
    ],

    [
        {'text' : '', 'type' : 'empty'},
        {'text' : '0', 'type' : 'number'},
        {'text' : '.', 'type' : 'number'},
        {'text' : '=', 'type' : 'equals'},
    ]
]


BUTTON_COLORS = {
    "number": "#3A3A3A",
    "operator": "#2563EB",
    "equals": "#16A34A",
    "clear": "#DC2626",
    "control": "#6B7280",
}

class CalculatorApp:


    def __init__(self):
        
        self.app = ctk.CTk()

        self.display = None

        self.calculator = Calculator()

        self.configure_window()
        
        self.configure_grid()

        self.create_display()

        self.create_buttons()

    def configure_window(self):
        
        self.app.title('Calculator')
        self.app.geometry('360x520')
        self.app.resizable(False, False)

    def create_display(self):

        self.display = ctk.CTkEntry(
            master=self.app,
            width=320,
            height=70,
            font=('Segoe UI', 30),
            justify='right',
        )

        self.display.insert(0, '0')

        self.display.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=20,
            pady=20,
            sticky='ew',
        )

    def configure_grid(self):

        for i in range(4):
            self.app.grid_columnconfigure(i, weight=1)

        for i in range(6):
            self.app.grid_rowconfigure(i, weight=1)

    def on_click_button(self, text):

        result = self.calculator.press(text)
        self.update_display(result)



    def update_display(self, text):

        self.display.delete(0, 'end')
        
        if text == '':
            text = '0'

        self.display.insert(0, text)


    def create_buttons(self):

        for row, row_data in enumerate(BUTTON_LAYOUT, start=1):

            for column, button_data in enumerate(row_data):

                if button_data['type'] == 'empty':
                    continue

                button_color = BUTTON_COLORS[button_data['type']]

                button = ctk.CTkButton(
                    master=self.app,
                    text=button_data['text'],
                    height=60,
                    font=("Segoe UI", 20),
                    fg_color=button_color,
                    command= lambda text=button_data['text'] : self.on_click_button(text),
                )

                button.grid(
                    row=row,
                    column=column,
                    padx=5,
                    pady=5,
                    sticky="nsew",
                )

    def run(self):

        self.app.mainloop()


# ----------------------------
# |          Theme           |
# ----------------------------
ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')


# ----------------------------
# |           Run            |
# ----------------------------
calculator = CalculatorApp() 
calculator.run()