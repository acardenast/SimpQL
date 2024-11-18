import tkinter as tk
import sqlparse
import pyperclip

# Función para eliminar saltos de línea y dejar todo en una sola línea - Function to remove line breaks and leave everything on one line
def simplify_to_single_line():
    sql_query = sql_entry.get("1.0", tk.END)
    sql_query = sql_query.strip().replace("\n", " ")
    sql_query = " ".join(sql_query.split())
    sql_entry.delete("1.0", tk.END)
    sql_entry.insert(tk.END, sql_query)

# Función para formatear la consulta SQL para SQL Management Studio - Function to format SQL query for SQL Management Studio
def format_for_sqlms():
    sql_query = sql_entry.get("1.0", tk.END)
    formatted_sql = sqlparse.format(sql_query, reindent=True, keyword_case='upper')
    sql_entry.delete("1.0", tk.END)
    sql_entry.insert(tk.END, formatted_sql)

# Funciones para los botones del menú - Functions for menu buttons
# Botón para eliminar todo salto de línea y formato - Button to remove all line breaks and formatting
def select_NoSQL():
    NoSQL_button.config(bg="#ADD8E6")  # Cambia el color del botón - Change the color of the button
    sqlms_button.config(bg=original_bg_color)
    simplify_to_single_line()
    sql_entry.tag_add("sel", "1.0", "end")  # Selecciona todo el texto - Select all text
    text_to_copy = sql_entry.get("1.0", tk.END).strip().replace("\n", "")  # Elimina saltos de línea - Remove line breaks
    sql_entry.clipboard_clear()  # Limpia el portapapeles - Clear the clipboard
    sql_entry.clipboard_append(text_to_copy)  # Copia el texto al portapapeles - Copy the text to the clipboard
    sql_entry.update()  # Actualiza el cuadro de entrada - Update the input box
    print("Seleccionado: NoSQL")

def select_sqlms():
    sqlms_button.config(bg="#ADD8E6")  # Cambia el color del botón - Change the color of the button
    NoSQL_button.config(bg=original_bg_color)
    format_for_sqlms()
    sql_entry.tag_add("sel", "1.0", "end")  # Selecciona todo el texto - Select all text
    text_to_copy = sql_entry.get("1.0", tk.END).strip().replace("\n", "")  # Elimina saltos de línea - Remove line breaks
    sql_entry.clipboard_clear()  # Limpia el portapapeles - Clear the clipboard
    sql_entry.clipboard_append(text_to_copy)  # Copia el texto al portapapeles - Copy the text to the clipboard
    sql_entry.update()  # Actualiza el cuadro de entrada - Update the input box
    print("Seleccionado: SQLMS")

# Crear la ventana principal - Create the main window
root = tk.Tk()
root.title("SQL Query Simplifier")
root.geometry("800x600")

# Guardar el color de fondo original de los botones - Save the original background color of the buttons
original_bg_color = root.cget("bg")

# Crear dos botones en la parte superior izquierda - Create two buttons on the top left
button_frame = tk.Frame(root)
button_frame.pack(anchor="nw", padx=10, pady=10)

NoSQL_button = tk.Button(button_frame, text="NoSQL", command=select_NoSQL)
NoSQL_button.grid(row=0, column=0, padx=5)
sqlms_button = tk.Button(button_frame, text="SQLMS", command=select_sqlms)
sqlms_button.grid(row=0, column=1, padx=5)

# Crear un cuadro de texto para ingresar la consulta SQL - Create a text box to enter the SQL query
sql_entry = tk.Text(root, wrap="word")
sql_entry.pack(expand=True, fill="both")

# Ejecutar el bucle principal de la aplicación - Run the main loop of the application
root.mainloop()
