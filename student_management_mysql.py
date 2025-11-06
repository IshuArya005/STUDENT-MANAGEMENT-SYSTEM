import tkinter as tk
from tkinter import messagebox
import mysql.connector


def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",       
            user="root",            
            password="Common@15",  
            database="student_db",
            port=3306  
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None


def add_student():
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()

    if name == "" or age == "" or course == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    conn = connect_db()
    if conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", (name, age, course))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student added successfully!")
        clear_fields()
        # show_students()

def show_students():
    listbox.delete(0, tk.END)
    conn = connect_db()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        for row in rows:
            listbox.insert(tk.END, f"ID:{row[0]} | Name:{row[1]} | Age:{row[2]} | Course:{row[3]}")
        conn.close()

def delete_student():
    selected = listbox.get(tk.ACTIVE)
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a record to delete")
        return

    student_id = selected.split('|')[0].split(':')[1].strip()
    conn = connect_db()
    if conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE id=%s", (student_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted", "Student record deleted")
        show_students()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Student Management System (MySQL)")
root.geometry("550x500")
root.config(bg="#e8f0f2")

# Title
tk.Label(root, text="Student Management System", font=("Arial", 18, "bold"), bg="#e8f0f2").pack(pady=10)

# Form Frame
form_frame = tk.Frame(root, bg="#e8f0f2")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#e8f0f2").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(form_frame, font=("Arial", 12))
entry_name.grid(row=0, column=1)

tk.Label(form_frame, text="Age:", font=("Arial", 12), bg="#e8f0f2").grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(form_frame, font=("Arial", 12))
entry_age.grid(row=1, column=1)

tk.Label(form_frame, text="Course:", font=("Arial", 12), bg="#e8f0f2").grid(row=2, column=0, padx=10, pady=5)
entry_course = tk.Entry(form_frame, font=("Arial", 12))
entry_course.grid(row=2, column=1)

# Buttons
btn_frame = tk.Frame(root, bg="#e8f0f2")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", font=("Arial", 12), bg="#4CAF50", fg="white", width=10, command=add_student).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="View All", font=("Arial", 12), bg="#2196F3", fg="white", width=10, command=show_students).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", font=("Arial", 12), bg="#F44336", fg="white", width=10, command=delete_student).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Clear", font=("Arial", 12), bg="#9E9E9E", fg="white", width=10, command=clear_fields).grid(row=0, column=3, padx=5)

# Listbox
listbox = tk.Listbox(root, width=65, height=12, font=("Arial", 12))
listbox.pack(pady=10)

show_students()  # display all records when program starts

root.mainloop()
