import tkinter as tk

root = tk.Tk()
root.title("简易计算器")
root.geometry('295x280+200+200')
root.attributes('-alpha', 0.9)
root["background"] = '#ffffff'
font = ('宋体', 20)
font16 = ('宋体', 16)

result_num = tk.StringVar()
result_num.set('')

tk.Label(root,
         textvariable=result_num, font=font, height=2,
         width=20, justify=tk.LEFT, anchor=tk.SE
         ).grid(row=1, column=1, columnspan=4)

button_clear = tk.Button(root, text="C", width=5, font=font16, relief=tk.FLAT, bg='#b1b2b2')
button_back = tk.Button(root, text="←", width=5, font=font16, relief=tk.FLAT, bg='#b1b2b2')
button_divide = tk.Button(root, text="/", width=5, font=font16, relief=tk.FLAT, bg='#b1b2b2')
button_multiply = tk.Button(root, text="*", width=5, font=font16, relief=tk.FLAT, bg='#b1b2b2')
button_clear.grid(row=2, column=1, padx=4, pady=2)
button_back.grid(row=2, column=2, padx=4, pady=2)
button_divide.grid(row=2, column=3, padx=4, pady=2)
button_multiply.grid(row=2, column=4, padx=4, pady=2)

button_seven = tk.Button(root, text="7", width=5, font=font16, relief=tk.FLAT, bg='#eacda1')
button_eight = tk.Button(root, text="8", width=5, font=font16, relief=tk.FLAT, bg='#eacda1')
button_nine = tk.Button(root, text="9", width=5, font=font16, relief=tk.FLAT, bg='#eacda1')
button_minus = tk.Button(root, text="-", width=5, font=font16, relief=tk.FLAT, bg='#b1b2b2')
button_seven.grid(row=3, column=1, padx=4, pady=2)
button_eight.grid(row=3, column=2, padx=4, pady=2)
button_nine.grid(row=3, column=3, padx=4, pady=2)
button_minus.grid(row=3, column=4, padx=4, pady=2)

button_four = tk.Button(root, text="4", width=5, font=font16, relief=tk.FLAT, bg='#eacda1')
button_five = tk.Button(root, text="5", width=5, font=font16, relief=tk.FLAT, bg='#eacda1')
button_six = tk.Button(root, text="6", width=5, font=font16, relief=tk.FLAT, bg='#eacda1')
button_plus = tk.Button(root, text="+", width=5, font=font16, relief=tk.FLAT, bg='#b1b2b2')
button_four.grid(row=4, column=1, padx=4, pady=2)
button_five.grid(row=4, column=2, padx=4, pady=2)
button_six.grid(row=4, column=3, padx=4, pady=2)
button_plus.grid(row=4, column=4, padx=4, pady=2)

button_one = tk.Button(root, text="1", width=5, font=font16, relief=tk.FLAT, bg='#eacda1')
button_two = tk.Button(root, text="2", width=5, font=font16, relief=tk.FLAT, bg='#eacda1')
button_three = tk.Button(root, text="3", width=5, font=font16, relief=tk.FLAT, bg='#eacda1')
button_equal1 = tk.Button(root, text="=", width=5, height=3, font=font16, relief=tk.FLAT, bg='#b1b2b2')
button_one.grid(row=5, column=1, padx=4, pady=2)
button_two.grid(row=5, column=2, padx=4, pady=2)
button_three.grid(row=5, column=3, padx=4, pady=2)
button_equal1.grid(row=5, column=4, padx=4, pady=2, rowspan=2)

button_zero1 = tk.Button(root, text="0", width=12, font=font16, relief=tk.FLAT, bg='#eacda1')
# button_zero2 = tk.Button(root, text="0", width=5, font=font16, relief=tk.FLAT, bg='#eacda1')
button_dot = tk.Button(root, text=".", width=5, font=font16, relief=tk.FLAT, bg='#eacda1')
# button_equal2 = tk.Button(root, text="=", width=5, font=font16, relief=tk.FLAT, bg='#b1b2b2')
button_zero1.grid(row=6, column=1, padx=4, pady=5, columnspan=2)
# button_zero2.grid(row=6, column=2, padx=4, pady=5)
button_dot.grid(row=6, column=3, padx=4, pady=5)
# button_equal2.grid(row=6, column=4, padx=4, pady=5)

'''点击事件'''


class Calculator:

    def __init__(self):
        self.flag = 0
        self.temp_str = ''
        self.result = ''

    def click_num_button(self, x):
        if not self.flag:
            result_num.set(result_num.get() + x)
        else:
            result_num.set('')
            result_num.set(result_num.get() + x)
        self.flag = 0

    def click_ope_button(self, x):
        result_num.set(result_num.get() + x)
        self.flag = 0

    def click_dot_button(self, x):
        if result_num.get() != "":
            result_num.set(result_num.get() + x)
        self.flag = 0

    def click_clear(self):
        result_num.set('')

    def click_back(self):
        result_num.set(result_num.get()[0:-1])

    def calculation(self):
        self.temp_str = result_num.get()
        self.result = eval(self.temp_str)
        result_num.set(str(self.result))
        self.flag = 1


mycalculator = Calculator()
button_one.config(command=lambda: mycalculator.click_num_button('1'))
button_two.config(command=lambda: mycalculator.click_num_button('2'))
button_three.config(command=lambda: mycalculator.click_num_button('3'))
button_four.config(command=lambda: mycalculator.click_num_button('4'))
button_five.config(command=lambda: mycalculator.click_num_button('5'))
button_six.config(command=lambda: mycalculator.click_num_button('6'))
button_seven.config(command=lambda: mycalculator.click_num_button('7'))
button_eight.config(command=lambda: mycalculator.click_num_button('8'))
button_nine.config(command=lambda: mycalculator.click_num_button('9'))
button_zero1.config(command=lambda: mycalculator.click_num_button('0'))
button_dot.config(command=lambda: mycalculator.click_dot_button('.'))
button_plus.config(command=lambda: mycalculator.click_ope_button('+'))
button_minus.config(command=lambda: mycalculator.click_ope_button('-'))
button_multiply.config(command=lambda: mycalculator.click_ope_button('*'))
button_divide.config(command=lambda: mycalculator.click_ope_button('/'))
button_equal1.config(command=mycalculator.calculation)
button_clear.config(command=mycalculator.click_clear)
button_back.config(command=mycalculator.click_back)

root.mainloop()
