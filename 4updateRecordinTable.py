# file: update_record_gui.py
import sqlite3
import tkinter as tk
from tkinter import messagebox

def update_record():
    db_file = "sampleDB.db"
    table_name = "sampleTable"
    record_id = int(entry_id.get())
    name = entry_name.get()
    address = entry_address.get()
    year = int(entry_year.get())
    color = entry_color.get()

    updated_values = (name, address, year, color)

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    try:
        cursor.execute(
            f"UPDATE {table_name} SET name = ?, address = ?, year = ?, color = ? WHERE id = ?;",
            (*updated_values, record_id),
        )
        conn.commit()
        messagebox.showinfo("Success", f"Record with ID {record_id} updated!")
        print(f"Record with ID {record_id} updated.")
        entry_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        entry_year.delete(0, tk.END)
        entry_color.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter correct data types.")
        print("Invalid input. Please enter correct data types.")

    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error updating record: {e}")
        conn.rollback()
        print(f"Error: {e}")

    finally:
        if conn:
            conn.close()

window = tk.Tk()
window.title("Update Record")

tk.Label(window, text="ID:").grid(row=0, column=0)
entry_id = tk.Entry(window)
entry_id.grid(row=0, column=1)

tk.Label(window, text="Name:").grid(row=1, column=0)
entry_name = tk.Entry(window)
entry_name.grid(row=1, column=1)

tk.Label(window, text="Address:").grid(row=2, column=0)
entry_address = tk.Entry(window)
entry_address.grid(row=2, column=1)

tk.Label(window, text="Year:").grid(row=3, column=0)
entry_year = tk.Entry(window)
entry_year.grid(row=3, column=1)

tk.Label(window, text="Color:").grid(row=4, column=0)
entry_color = tk.Entry(window)
entry_color.grid(row=4, column=1)

tk.Button(window, text="Update", command=update_record).grid(row=5, column=1)

window.mainloop()