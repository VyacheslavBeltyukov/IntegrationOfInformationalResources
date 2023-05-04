import json
import requests
from tkinter import Frame, Entry, Label, ttk, Tk, StringVar


def on_button_click():
    s_body = {'NumberToWords': 'ubiNum', 'NumberToDollars': 'dNum'}

    # Основне тіло запиту
    url = f"https://www.dataaccess.com/webservicesserver/NumberConversion.wso/{dropdown_var.get()}"
    headers = {'content-type': 'application/json'}
    if dropdown_var.get() == 'NumberToDollars':
        number = float(input_var.get())
    else:
        number = int(input_var.get())

    body = {
        f"{s_body[dropdown_var.get()]}": number
    }
    body = json.dumps(body)

    # Відправка запиту
    response = requests.post(url, data=body, headers=headers)

    # Вивід результату в текстове поле
    label_res.config(text="Result is: " + response.text)


if __name__ == '__main__':
    root = Tk()
    root.title('REST client UI')
    root.geometry('280x110')
    root.resizable(width=False, height=False)

    # Створення змінної для збереження вибраного параметра
    dropdown_var = StringVar()

    mainFrame = Frame(root)
    mainFrame.grid(row=1, column=1, padx=5, pady=5)

    # Створення віджету випадного меню
    dropdown = ttk.Combobox(mainFrame, textvariable=dropdown_var)
    dropdown['values'] = ('NumberToWords', 'NumberToDollars')
    dropdown.grid(row=1, column=2, pady=5)

    # Створення надпису
    label = Label(mainFrame, text="Select option: ")
    label.grid(row=1, column=1, pady=5)

    # Створення надпису, що в подальшому буде містити результат
    label_res = Label(root, text="Result is: ")
    label_res.grid(row=2, column=1, pady=5)

    # Створення поля вводу для чисел
    input_var = StringVar()
    pathInput = Entry(mainFrame, width=10, textvariable=input_var, relief="flat", highlightbackground="black",
                      highlightthickness=1, bd=0)
    pathInput.grid(row=2, column=1, pady=5)

    # Створення кнопки для здійснення запиту
    button = ttk.Button(mainFrame, text="Send request!", command=on_button_click)
    button.grid(row=2, column=2, pady=5)

    # Запуск основного циклу
    root.mainloop()
