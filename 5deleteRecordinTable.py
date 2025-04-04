# file: delete_record_gui.py
import sqlite3
import tkinter as tk
from tkinter import messagebox

def delete_record():
    db_file = "sampleDB.db"
    table_name = "sampleTable"
    record_id = int(entry_id.get())

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    try:
        cursor.execute(f"DELETE FROM {table_name} WHERE id = ?;", (record_id,))
        conn.commit()
        messagebox.showinfo("Success", f"Record with ID {record_id} deleted!")
        print(f"Record with ID {record_id} deleted.")
        entry_id.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter an integer ID.")
        print("Invalid input. Please enter an integer ID.")

    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error deleting record: {e}")
        conn.rollback()
        print(f"Error: {e}")

    finally:
        if conn:
            conn.close()

window = tk.Tk()
window.title("Delete Record")

tk.Label(window, text="ID:").grid(row=0, column=0)
entry_id = tk.Entry(window)
entry_id.grid(row=0, column=1)

tk.Button(window, text="Delete", command=delete_record).grid(row=1, column=1)

window.mainloop()