import tkinter as tk
import pandas as pd

def what_to_do(statistics = None):
    root = tk.Tk()

    if statistics is not None:
        label = tk.Label(root, text=statistics + '\nWhat do you want to do?')
        label.pack()
    else:
        label = tk.Label(root, text='What do you want to do?')
        label.pack()

    root.title('What to do?')
    output = []

    def on_button_click(choice):
        output.append(choice)
        root.destroy()
    
    button1 = tk.Button(root, text="Mark words I know", command=lambda: on_button_click('mark knowns'))
    button1.pack()
    button2 = tk.Button(root, text="Quiz me on words I don\'t know", command=lambda: on_button_click('quiz'))
    button2.pack()

    root.mainloop()

    return output[0]

def ask_if_words_are_known(words):
    root = tk.Tk()
    root.title('Do you know these words?')
    current_word_index = 0
    num_words = len(words)
    output = []

    def on_button_click(choice):
        nonlocal current_word_index
        output.append(choice)
        current_word_index += 1
        if current_word_index < num_words:
            label.config(text=f'Do you know the word:\n{words[current_word_index]}')
        else: 
            root.destroy()

    label = tk.Label(root, text=f'Do you know the meaning of the word:\n\n{words[current_word_index]}\n')
    label.pack()

    button1 = tk.Button(root, text="Yes", command=lambda: on_button_click(True))
    button1.pack()
    button2 = tk.Button(root, text="No", command=lambda: on_button_click(False))
    button2.pack()

    root.mainloop()

    return output

def quiz_on_words(words, translations):
    root = tk.Tk()
    root.title('Vocab quiz')
    current_word_index = 0
    num_words = len(words)
    output = []
    translations = [', '.join(translation) for translation in translations]

    def check_translation(event=None):
        nonlocal current_word_index
        user_input = entry.get().strip().lower()
        if user_input in translations[current_word_index].lower():
            output.append(True)
        else:
            output.append(False)
        current_word_index += 1
        if current_word_index < num_words:
            label.config(text=f'What is the translation of:\n{words[current_word_index]}')
            entry.delete(0, tk.END)
        else: 
            root.destroy()

    label = tk.Label(root, text=f'What is the translation of:\n\n{words[current_word_index]}\n')
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    entry.bind('<Return>', check_translation)

    root.mainloop()

    return output


if __name__ == '__main__':
    # print(ask_if_words_are_known(['a', 'b', 'c']))
    # print(quiz_on_words(['a', 'b', 'c'], ['1', '2', '3']))
    print(what_to_do('statsssss'))