import csv
import json
import tkinter as tk
from tkinter import PhotoImage
import pyttsx3

def speak_ingredients(ingredients):
    engine = pyttsx3.init()  
    engine.say(ingredients)  
    engine.runAndWait()

search_results_frame = None  

def load_recipes():
    with open('swaad.json', 'r') as jsonfile:
        recipes_data = json.load(jsonfile)
    
    recipes = []
    for recipe in recipes_data:
        recipes.append({
            'Recipe Name': recipe['Title'],
            'Ingredients': recipe['Ingredients'],
            'Instructions': recipe['Instructions']
        })
    
    return recipes
    

def search_recipes_by_name(recipes, query):
    results = []
    for recipe in recipes:
        if query.lower() in recipe['Recipe Name'].lower():
            results.append(recipe)
    return results

import tkinter as tk

def display_recipe_in_gui(recipe):
    recipe_window = tk.Toplevel()
    recipe_window.title(recipe['Recipe Name'])
    recipe_window.configure(bg='#F2ea6b')
    recipe_window.geometry("900x750")
    
    canvas = tk.Canvas(recipe_window, bg='#F2ea6b', highlightthickness=0)
    vertical_scrollbar = tk.Scrollbar(recipe_window, orient='vertical', command=canvas.yview)
    horizontal_scrollbar = tk.Scrollbar(recipe_window, orient='horizontal', command=canvas.xview)

    canvas.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)

    canvas.pack(side='left', fill='both', expand=True)
    vertical_scrollbar.pack(side='right', fill='y')
    horizontal_scrollbar.pack(side='bottom', fill='x')
    

    frame = tk.Frame(canvas, bg='#F2ea6b')
    canvas.create_window((0, 0), window=frame, anchor='nw')
    
    def update_scrollregion(event=None):
        canvas.configure(scrollregion=canvas.bbox('all'))
    
    
    frame.bind('<Configure>', update_scrollregion)
    recipe_name_label = tk.Label(frame, text="Recipe Name: " + recipe['Recipe Name'], font=('Helvetica', 30, 'bold'), bg='#F2ea6b', fg='black')
    recipe_name_label.pack(pady=(10, 5))
    
    ingredients_text = recipe['Ingredients'].replace('▢', '\n\n▢')
    speak_button = tk.Button(frame, text="Speak Ingredients", command=lambda: speak_ingredients(recipe['Ingredients']))
    speak_button.pack(pady=(0, 10))
    ingredients_label = tk.Label(frame, text="Ingredients:\n\n" + ingredients_text, font=('Helvetica', 21), wraplength=1500, bg='#F2ea6b', justify='left')
    ingredients_label.pack(pady=(10, 10))
    
    instructions_text = recipe['Instructions'].replace('.', '\n\n')
    instructions_label = tk.Label(frame, text=" \npInstructions:\n\n" + instructions_text, font=('Helvetica', 21), wraplength=1500, bg='#F2ea6b', justify='left')
    instructions_label.pack(pady=(0, 10))

def search_recipe():
    global search_results_frame 
    query = search_entry.get()
    search_results = search_recipes_by_name(recipes, query)
    if len(search_results) == 0:
        search_results_label.config(text="No recipes found matching the given name.", fg='red')
    else:
        search_results_label.config(text="")
        if search_results_frame:
            search_results_frame.destroy() 
        
        search_results_frame = tk.Frame(root)
        canvas = tk.Canvas(search_results_frame)
        scrollbar = tk.Scrollbar(search_results_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        for i, recipe in enumerate(search_results):
            recipe_button = tk.Button(scrollable_frame, text=recipe['Recipe Name'], font=('Helvetica', 10, 'bold'), command=lambda r=recipe: display_recipe_in_gui(r))
            recipe_button.pack(padx=10, pady=5, fill=tk.X)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        search_results_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)


if __name__ == "__main__":
    recipes = load_recipes()
    
    root = tk.Tk()
    root.title("Swaadishta-the great indian taste")
    root.geometry("900x750")
    imag_path=PhotoImage(file=r"C:\Users\ktgol\OneDrive\Desktop\mini\cooking.png")
    bg_image=tk.Label(root,image=imag_path)
    bg_image.place(relheight=1,relwidth=1)
    text_label = tk.Label(root, text="Swaadishta", font=('Devanagari MT', 50), fg='goldenrod1', bg='#2f2e34')
    text_label.place(relx=0.5, rely=0.17, anchor='center')
    tx_label = tk.Label(root, text="তততততততততততততততততততততততত", font=('Devanagari MT', 15), fg='goldenrod1', bg='#2f2e34')
    tx_label.place(relx=0.5, rely=0.24, anchor='center')
    tt_label=tk.Label(root,text="||  The Great Indian Taste  ||",font=('Gautami', 25), fg='goldenrod1', bg='#2f2e34')
    tt_label.place(relx=0.5, rely=0.3, anchor='center')
    t_label=tk.Label(root,text="..............................................................",font=('Gautami', 15), fg='goldenrod1', bg='#2f2e34')
    t_label.place(relx=0.5, rely=0.37, anchor='center')
    to_label=tk.Label(root,text="Search recipes by Name",font=('Gautami', 15), fg='goldenrod1', bg='#2f2e34')
    to_label.place(relx=0.5, rely=0.38, anchor='center')
    search_frame = tk.Frame(root, bg="#2f2e34")  
    search_frame.pack(pady=(10, 0))

    search_entry = tk.Entry(search_frame, font=('Helvetica', 15), width=30, bd=0, highlightthickness=0)
    search_entry.grid(row=0, column=0, padx=10, pady=5)

    search_button = tk.Button(search_frame, text="Search", font=('Helvetica', 12, 'bold'), command=search_recipe)
    search_button.grid(row=0, column=1, padx=10, pady=5)
    
    search_results_label = tk.Label(root, text="", font=('Helvetica', 12), fg='red')
    search_results_label.pack()
   
    root.update_idletasks()
    search_frame.place(relx=0.5, rely=0.43, anchor=tk.CENTER)
    root.mainloop()

