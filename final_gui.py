from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, ttk, Scrollbar, VERTICAL, HORIZONTAL

import pymysql

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\aupp_school project\SURVEY\gp_project_1\build\assets")

FRAME0_PATH = ASSETS_PATH / Path("frame0")
FRAME1_PATH = ASSETS_PATH / Path("frame1")
FRAME3_PATH = ASSETS_PATH / Path("frame3")
FRAME4_PATH = ASSETS_PATH / Path("frame4")
FRAME5_PATH = ASSETS_PATH / Path("frame5")
FRAME6_PATH = ASSETS_PATH / Path("frame6")
FRAME7_PATH = ASSETS_PATH / Path("frame7")
FRAME8_PATH = ASSETS_PATH / Path("frame8")


def relative_to_assets(base_path: Path, path: str) -> Path:
    return base_path / Path(path)


window = Tk()
window.geometry("800x600")
window.configure(bg="#FFFFFF")


def login_gui():
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=600,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(FRAME0_PATH, "image_1.png"))
    image_1 = canvas.create_image(
        390.0,
        300.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets(FRAME0_PATH, "entry_1.png"))
    entry_bg_1 = canvas.create_image(
        402.5,
        268.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=278.0,
        y=244.0,
        width=249.0,
        height=47.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets(FRAME0_PATH, "entry_2.png"))
    entry_bg_2 = canvas.create_image(
        402.5,
        381.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        show="*"
    )
    entry_2.place(
        x=278.0,
        y=357.0,
        width=249.0,
        height=46.0
    )

    def compare_login():
        try:
            connection = pymysql.connect(host='127.0.0.1',
                                         user='root',
                                         password='nhalanhly',
                                         db='LIBRARY')

            select = "SELECT * FROM ADMIN WHERE ID = %s AND PASSWORD = %s"
            cursor = connection.cursor()
            cursor.execute(select, (entry_1.get(), entry_2.get()))
            result = cursor.fetchall()
            if result:
                print("Login success")
                menu_gui()
            else:
                print("Login failed")
                messagebox.showerror("Error", "ID OR password invalid")
        except Exception as e:
            print(e)

    button_image_1 = PhotoImage(
        file=relative_to_assets(FRAME0_PATH, "button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=compare_login,
        relief="flat"
    )
    button_1.place(
        x=352.0,
        y=461.0,
        width=96.27217864990234,
        height=44.0
    )

    window.resizable(False, False)
    window.mainloop()


def register_gui():
    def register_user(entry_1, entry_2, entry_3):
        conn = None
        try:
            connection = pymysql.connect(host='127.0.0.1',
                                         user='root',
                                         password='nhalanhly',
                                         db='LIBRARY')
            user_id = int(entry_1)
            name = entry_2
            password = entry_3
            insert = "INSERT INTO REGISTERED (USER_ID, NAME, PASSWORD) VALUES (%s, %s, %s)"
            cursor = connection.cursor()
            cursor.execute(insert, (user_id, name, password))
            connection.commit()
            connection.close()
            print("Register success")
            messagebox.showinfo("Success", "Register success")
        except Exception as e:
            print(e)
            messagebox.showerror("Input Error", "Register failed")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=600,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(FRAME1_PATH, "image_1.png"))
    image_1 = canvas.create_image(
        390.0,
        300.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(FRAME1_PATH, "button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: register_user(entry_1.get(), entry_2.get(), entry_3.get()),
        relief="flat"
    )
    button_1.place(
        x=331.0,
        y=461.0,
        width=143.0,
        height=40.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(FRAME1_PATH, "button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=menu_gui,
        relief="flat"
    )
    button_2.place(
        x=557.0,
        y=22.0,
        width=191.0,
        height=68.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets(FRAME1_PATH, "entry_1.png"))
    entry_bg_1 = canvas.create_image(
        402.5,
        264.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=278.0,
        y=240.0,
        width=249.0,
        height=47.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets(FRAME1_PATH, "entry_2.png"))
    entry_bg_2 = canvas.create_image(
        402.5,
        324.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=278.0,
        y=300.0,
        width=249.0,
        height=47.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets(FRAME1_PATH, "entry_3.png"))
    entry_bg_3 = canvas.create_image(
        402.5,
        381.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=278.0,
        y=357.0,
        width=249.0,
        height=46.0
    )
    window.resizable(False, False)
    window.mainloop()


def borrow_return_gui():
    def borrow_book(entry_1, entry_2):
        conn = None
        try:
            connection = pymysql.connect(host='127.0.0.1',
                                         user='root',
                                         password='nhalanhly',
                                         db='LIBRARY')
            cursor = connection.cursor()

            book_code = int(entry_1)
            user_id = int(entry_2)

            select_from_book_list = "SELECT * FROM BOOK_LIST WHERE book_code = %s"
            select_from_registered = "SELECT * FROM REGISTERED WHERE USER_ID = %s"
            select_availability_from_books = "SELECT AVAILIBILITY FROM BOOKS WHERE book_code = %s"

            cursor.execute(select_from_book_list, (book_code))
            book_result = cursor.fetchall()

            cursor.execute(select_from_registered, (user_id))
            student_result = cursor.fetchall()

            cursor.execute(select_availability_from_books, (book_code))
            book_status = cursor.fetchall()

            print(book_result)
            print(student_result)

            book_code = book_result[0][0]
            tittle = book_result[0][1]
            author = book_result[0][2]
            publish_year = book_result[0][3]
            borrower_id = student_result[0][0]
            borrower_name = student_result[0][1]

            if book_status[0][0] == "YES":
                insert_to_borrowed = "INSERT INTO BORROW_LIST (BOOK_ID, TITTLE, AUTHOR, PUBLISH_YEAR, BORROWER_ID, BORROWER_NAME) VALUES (%s, %s, %s, %s, %s, %s)"
                update_books = "UPDATE BOOKS SET AVAILIBILITY = 'NO' WHERE BOOK_CODE = %s"
                cursor.execute(insert_to_borrowed, (book_code, tittle, author, publish_year, borrower_id, borrower_name))
                cursor.execute(update_books, (book_code))
                print("Borrow book success")
                messagebox.showinfo("Success", "Borrow book success")
            else:
                messagebox.showerror("Fail", "Book is already borrowed")
            connection.commit()
            connection.close()

        except Exception as e:
            print(e)
            messagebox.showinfo("Error", str(e))

    def return_book(entry_1, entry_2):
        conn = None
        try:
            connection = pymysql.connect(host='127.0.0.1',
                                         user='root',
                                         password='nhalanhly',
                                         db='LIBRARY')
            cursor = connection.cursor()

            book_code = int(entry_1)
            user_id = int(entry_2)

            select_from_book_list = "SELECT * FROM BOOK_LIST WHERE book_code = %s"
            select_from_registered = "SELECT * FROM REGISTERED WHERE USER_ID = %s"
            select_availability_from_books = "SELECT AVAILIBILITY FROM BOOKS WHERE book_code = %s"

            cursor.execute(select_from_book_list, (book_code))
            book_result = cursor.fetchall()

            cursor.execute(select_from_registered, (user_id))
            student_result = cursor.fetchall()

            cursor.execute(select_availability_from_books, (book_code))
            book_status = cursor.fetchall()

            print(book_result)
            print(student_result)

            book_code = book_result[0][0]
            tittle = book_result[0][1]
            author = book_result[0][2]
            publish_year = book_result[0][3]
            borrower_id = student_result[0][0]
            borrower_name = student_result[0][1]

            if book_status[0][0] == "NO":
                insert_to_return = "INSERT INTO RETURN_LIST (BOOK_ID, TITTLE, AUTHOR, PUBLISH_YEAR, RETURNER_ID, RETURNER_NAME) VALUES (%s, %s, %s, %s, %s, %s)"
                update_books = "UPDATE BOOKS SET AVAILIBILITY = 'YES' WHERE BOOK_CODE = %s"
                cursor.execute(insert_to_return, (book_code, tittle, author, publish_year, borrower_id, borrower_name))
                cursor.execute(update_books, (book_code))
                messagebox.showinfo("Success", "Book returned success")
                print("Return book success")
            else:
                messagebox.showerror("Fail", "Book is already returned")
            connection.commit()
            connection.close()

        except Exception as e:
            print(e)

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=600,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(FRAME4_PATH, "image_1.png"))
    image_1 = canvas.create_image(
        400.0,
        58.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets(FRAME4_PATH, "image_2.png"))
    image_2 = canvas.create_image(
        238.0,
        324.0,
        image=image_image_2
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets(FRAME4_PATH, "entry_1.png"))
    entry_bg_1 = canvas.create_image(
        627.5,
        324.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=496.0,  # 496.0
        y=142.0,
        width=263.0,
        height=362.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(FRAME4_PATH, "button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: borrow_book(entry_2.get(), entry_3.get()),
        relief="flat"
    )
    button_1.place(
        x=69.0,
        y=520.0,
        width=160.0,
        height=58.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(FRAME4_PATH, "button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: return_book(entry_2.get(), entry_3.get()),
        relief="flat"
    )
    button_2.place(
        x=247.0,  # 247.0
        y=520.0,
        width=160.0,
        height=58.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(FRAME4_PATH, "button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=menu_gui,
        relief="flat"
    )
    button_3.place(
        x=569.0,
        y=520.0,
        width=160.0,
        height=58.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets(FRAME4_PATH, "entry_2.png"))
    entry_bg_2 = canvas.create_image(
        235.5,
        261.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=149.5,  # 149.5
        y=238.5,
        width=172.0,
        height=44.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets(FRAME4_PATH, "entry_3.png"))
    entry_bg_3 = canvas.create_image(
        238.0,
        415.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=152.0,
        y=392.0,
        width=172.0,
        height=44.0
    )
    window.resizable(False, False)
    window.mainloop()


def add_remove_gui():
    def add_book(entry_5, entry_4, entry_3, entry_2):
        conn = None
        try:
            connection = pymysql.connect(host='127.0.0.1',
                                         user='root',
                                         password='nhalanhly',
                                         db='LIBRARY')

            book_code = int(entry_5)
            tittle = entry_4
            author = entry_3
            publish_year = int(entry_2)
            availibility = "YES"

            insert_to_book_list = "INSERT INTO BOOK_LIST (book_code, tittle, author, publish_year) VALUES (%s, %s, %s, %s)"
            insert_to_books = "INSERT INTO BOOKS (book_code, tittle, author, publish_year, availibility) VALUES (%s, %s, %s, %s, %s)"
            cursor = connection.cursor()
            cursor.execute(insert_to_book_list, (book_code, tittle, author, publish_year))
            cursor.execute(insert_to_books, (book_code, tittle, author, publish_year, availibility))
            connection.commit()
            connection.close()
            print("Add book success")
            messagebox.showinfo("Success", "Add book success")
        except Exception as e:
            print(e)
            messagebox.showerror("Error", e)

    def remove_book(entry_1):
        conn = None
        try:
            connection = pymysql.connect(host='127.0.0.1',
                                         user='root',
                                         password='nhalanhly',
                                         db='LIBRARY')
            book_code = int(entry_1)
            # compare book_code in SHELVE. if there is, then delete
            delete_from_book_list = "DELETE FROM BOOK_LIST WHERE book_code = %s"
            delete_from_books = "DELETE FROM BOOKS WHERE book_code = %s"

            cursor = connection.cursor()
            cursor.execute(delete_from_book_list, (book_code))
            cursor.execute(delete_from_books, (book_code))
            connection.commit()
            connection.close()
            print("Remove book success")
            messagebox.showinfo("Success", "Remove book success")
        except Exception as e:
            print(e)
            messagebox.showerror("Error", e)

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=600,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(FRAME3_PATH, "image_1.png"))
    image_1 = canvas.create_image(
        400.0,
        58.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets(FRAME3_PATH, "image_2.png"))
    image_2 = canvas.create_image(
        244.0,
        324.0,
        image=image_image_2
    )

    canvas.create_rectangle(
        480.0,
        142.0,
        775.0,
        506.0,
        fill="#D9D9D9",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets(FRAME3_PATH, "button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: remove_book(entry_1.get()),
        relief="flat"
    )
    button_1.place(
        x=547.0,
        y=515.0,
        width=150.0,
        height=47.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(FRAME3_PATH, "button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=menu_gui,
        relief="flat"
    )
    button_2.place(
        x=320.0,
        y=530.0,
        width=145.0,
        height=58.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(FRAME3_PATH, "button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_book(entry_5.get(), entry_4.get(), entry_3.get(), entry_2.get()),
        relief="flat"
    )
    button_3.place(
        x=92.0,
        y=506.0,
        width=160.0,
        height=58.0
    )

    canvas.create_text(
        552.0,
        187.0,
        anchor="nw",
        text="Book Code: ",
        fill="#000000",
        font=("JostRoman Regular", 30 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets(FRAME3_PATH, "entry_1.png"))
    entry_bg_1 = canvas.create_image(
        627.0,
        324.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=541.0,
        y=301.0,
        width=172.0,
        height=44.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets(FRAME3_PATH, "entry_2.png"))
    entry_bg_2 = canvas.create_image(
        244.0,
        464.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=158.0,
        y=446.0,
        width=172.0,
        height=34.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets(FRAME3_PATH, "entry_3.png"))
    entry_bg_3 = canvas.create_image(
        244.0,
        383.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=158.0,
        y=365.0,
        width=172.0,
        height=34.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets(FRAME3_PATH, "entry_4.png"))
    entry_bg_4 = canvas.create_image(
        244.0,
        303.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=158.0,
        y=285.0,
        width=172.0,
        height=34.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets(FRAME3_PATH, "entry_5.png"))
    entry_bg_5 = canvas.create_image(
        244.0,
        230.0,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=158.0,
        y=212.0,
        width=172.0,
        height=34.0
    )
    window.resizable(False, False)
    window.mainloop()


def search_gui():
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=600,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    canvas.create_rectangle(
        0.0,
        117.0,
        202.0,
        600.0,
        fill="#D9D9D9",
        outline=""
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets(FRAME5_PATH, "entry_1.png"))
    entry_bg_1 = canvas.create_image(
        114.0,
        188.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=66.0,
        y=167.0,
        width=96.0,
        height=40.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets(FRAME5_PATH, "entry_2.png"))
    entry_bg_2 = canvas.create_image(
        114.0,
        338.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=66.0,
        y=317.0,
        width=96.0,
        height=40.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets(FRAME5_PATH, "entry_3.png"))
    entry_bg_3 = canvas.create_image(
        114.0,
        488.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=66.0,
        y=467.0,
        width=96.0,
        height=40.0
    )

    canvas.create_text(
        42.0,
        137.0,
        anchor="nw",
        text="Search by Title:",
        fill="#000000",
        font=("JostRoman Regular", 20 * -1)
    )

    canvas.create_text(
        30.0,
        289.0,
        anchor="nw",
        text="Search by Author:",
        fill="#000000",
        font=("JostRoman Regular", 20 * -1)
    )

    canvas.create_text(
        41.0,
        438.0,
        anchor="nw",
        text="Search by Year:",
        fill="#000000",
        font=("JostRoman Regular", 20 * -1)
    )

    canvas.create_text(
        471.0,
        127.0,
        anchor="nw",
        text="Book list:",
        fill="#000000",
        font=("JostRoman Regular", 20 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets(FRAME5_PATH, "image_1.png"))
    image_1 = canvas.create_image(
        400.0,
        58.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets(FRAME5_PATH, "image_2.png"))
    image_2 = canvas.create_image(
        502.0,
        368.0,
        image=image_image_2
    )

    def fetch_all_data():
        try:
            conn = None
            conn = pymysql.connect(host='127.0.0.1',
                                   user='root',
                                   password='nhalanhly',
                                   db='LIBRARY')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM BOOKS')
            row = cursor.fetchall()
            return row
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()

    def insert_data(tree, rows):
        for row in rows:
            tree.insert('', 'end', values=row)

    columns = ("Code", "Title", "Author", "Year", "Availability")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=15)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")

    tree.place(x=200, y=150, width=580, height=430)

    vsb = Scrollbar(window, orient=VERTICAL, command=tree.yview)
    vsb.place(x=780, y=150, height=430)
    tree.configure(yscrollcommand=vsb.set)

    hsb = Scrollbar(window, orient=HORIZONTAL, command=tree.xview)
    hsb.place(x=200, y=580, width=580)
    tree.configure(xscrollcommand=hsb.set)

    rows = fetch_all_data()
    insert_data(tree, rows)

    def fill_up_title(tree, titles):
        tree.delete(*tree.get_children())
        rows = search_by_title(titles)
        insert_data(tree, rows)

    def search_by_title(title):
        try:
            conn = None
            conn = pymysql.connect(host='127.0.0.1',
                                   user='root',
                                   password='nhalanhly',
                                   db='LIBRARY')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM BOOKS WHERE TITTLE LIKE '%{title}%'")
            row = cursor.fetchall()
            return row
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()

    button_image_1 = PhotoImage(
        file=relative_to_assets(FRAME5_PATH, "button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fill_up_title(tree, entry_1.get()),
        relief="flat"
    )
    button_1.place(
        x=17.0,
        y=176.0,
        width=28.09027862548828,
        height=22.5
    )

    def search_by_author(author):
        try:
            conn = None
            conn = pymysql.connect(host='127.0.0.1',
                                   user='root',
                                   password='nhalanhly',
                                   db='LIBRARY')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM BOOKS WHERE AUTHOR LIKE '%{author}%'")
            row = cursor.fetchall()
            return row
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()

    def fill_up_author(tree, author):
        tree.delete(*tree.get_children())
        rows = search_by_author(author)
        insert_data(tree, rows)

    button_image_2 = PhotoImage(
        file=relative_to_assets(FRAME5_PATH, "button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fill_up_author(tree, entry_2.get()),
        relief="flat"
    )
    button_2.place(
        x=17.0,
        y=327.0,
        width=28.09027862548828,
        height=22.5
    )

    def search_by_year(year):
        try:
            conn = None
            conn = pymysql.connect(host='127.0.0.1',
                                   user='root',
                                   password='nhalanhly',
                                   db='LIBRARY')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM BOOKS WHERE PUBLISH_YEAR LIKE '%{year}%'")
            row = cursor.fetchall()
            return row
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()

    def fill_up_year(tree, year):
        tree.delete(*tree.get_children())
        rows = search_by_year(year)
        insert_data(tree, rows)

    button_image_3 = PhotoImage(
        file=relative_to_assets(FRAME5_PATH, "button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: fill_up_year(tree, int(entry_3.get())),
        relief="flat"
    )
    button_3.place(
        x=17.0,
        y=477.0,
        width=28.09027862548828,
        height=22.5
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets(FRAME5_PATH, "button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=menu_gui,
        relief="flat"
    )
    button_4.place(
        x=577.0,
        y=22.0,
        width=165.0,
        height=60.0
    )

    window.resizable(True, True)
    window.mainloop()


def menu_gui():
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=600,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(FRAME6_PATH, "image_1.png"))
    image_1 = canvas.create_image(
        400.0,
        58.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(FRAME6_PATH, "button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=login_gui,
        relief="flat"
    )
    button_1.place(
        x=289.0,
        y=511.0,
        width=222.0,
        height=66.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(FRAME6_PATH, "button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=return_record_gui,
        relief="flat"
    )
    button_2.place(
        x=488.0,
        y=398.0,
        width=222.0,
        height=66.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(FRAME6_PATH, "button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=add_remove_gui,
        relief="flat"
    )
    button_3.place(
        x=488.0,
        y=285.0,
        width=222.0,
        height=66.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets(FRAME6_PATH, "button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=search_gui,
        relief="flat"
    )
    button_4.place(
        x=488.0,
        y=172.0,
        width=222.0,
        height=66.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets(FRAME6_PATH, "button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=borrow_record_gui,
        relief="flat"
    )
    button_5.place(
        x=90.0,
        y=398.0,
        width=222.0,
        height=66.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets(FRAME6_PATH, "button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=borrow_return_gui,
        relief="flat"
    )
    button_6.place(
        x=90.0,
        y=285.0,
        width=222.0,
        height=66.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets(FRAME6_PATH, "button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=register_gui,
        relief="flat"
    )
    button_7.place(
        x=90.0,
        y=172.0,
        width=222.0,
        height=66.0
    )
    window.resizable(False, False)
    window.mainloop()


def borrow_record_gui():
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=600,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(FRAME7_PATH, "image_1.png"))
    image_1 = canvas.create_image(
        400.0,
        58.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(FRAME7_PATH, "button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=menu_gui,
        relief="flat"
    )
    button_1.place(
        x=599.0,
        y=20.0,
        width=168.0,
        height=60.0
    )

    columns = ("Code", "Title", "Author", "Borrower ID", "Name", "Borrow Date")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=15)

    def fetch_all_borrow():
        try:
            conn = None
            conn = pymysql.connect(host='127.0.0.1',
                                   user='root',
                                   password='nhalanhly',
                                   db='LIBRARY')
            cursor = conn.cursor()
            cursor.execute('SELECT book_id, tittle, author, borrower_id, borrower_name, REGDATETIME FROM BORROW_LIST')
            row = cursor.fetchall()
            return row
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()

    def insert_data(tree, rows):
        for row in rows:
            tree.insert('', 'end', values=row)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")

    tree.place(x=0, y=115, width=780, height=470)

    vsb = Scrollbar(window, orient=VERTICAL, command=tree.yview)
    vsb.place(x=780, y=110, height=470)
    tree.configure(yscrollcommand=vsb.set)

    hsb = Scrollbar(window, orient=HORIZONTAL, command=tree.xview)
    hsb.place(x=0, y=580, width=780)
    tree.configure(xscrollcommand=hsb.set)

    rows = fetch_all_borrow()
    insert_data(tree, rows)

    window.resizable(False, False)
    window.mainloop()


def return_record_gui():
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=600,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(FRAME8_PATH, "image_1.png"))
    image_1 = canvas.create_image(
        400.0,
        58.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(FRAME8_PATH, "button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=menu_gui,
        relief="flat"
    )
    button_1.place(
        x=599.0,
        y=20.0,
        width=168.0,
        height=60.0
    )

    def fetch_all_return():
        try:
            conn = None
            conn = pymysql.connect(host='127.0.0.1',
                                   user='root',
                                   password='nhalanhly',
                                   db='LIBRARY')
            cursor = conn.cursor()
            cursor.execute('SELECT book_id, tittle, author, returner_id, returner_name, REGDATETIME FROM RETURN_LIST')
            row = cursor.fetchall()
            return row
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()

    def insert_data(tree, rows):
        for row in rows:
            tree.insert('', 'end', values=row)

    columns = ("Code", "Title", "Author", "Returner ID", "Name", "Return Date")
    tree = ttk.Treeview(window, columns=columns, show="headings", height=15)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")

    tree.place(x=0, y=115, width=780, height=470)

    vsb = Scrollbar(window, orient=VERTICAL, command=tree.yview)
    vsb.place(x=780, y=110, height=470)
    tree.configure(yscrollcommand=vsb.set)

    hsb = Scrollbar(window, orient=HORIZONTAL, command=tree.xview)
    hsb.place(x=0, y=580, width=780)
    tree.configure(xscrollcommand=hsb.set)

    rows = fetch_all_return()
    insert_data(tree, rows)

    window.resizable(False, False)
    window.mainloop()
