from flask import *
import sqlite3

app = Flask(__name__)
DATABASE = 'CRUD.db'


# Handlers ==>
'''
def calculate_loss(amount, duration, working_time):
    yourprofit = (working_time/duration)*100
    yourloss = 100 - (working_time/duration)*100
    amountloss = amount*(yourloss/100)
    return yourloss
'''

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/savedetails", methods=["POST"])
def saveDetails():
    msg = "msg"
    name = request.form["name"]
    location = (request.form["location"])
    email_id = (request.form["email_id"])
    
    with sqlite3.connect("CRUD.db") as con:
        try:
            cur = con.cursor()
            cur.execute("INSERT into CRUD_for_user_info (NAME, LOCATION , EMAIL_ID) values (?,?,?)",
                        (name, location , email_id))
            con.commit()
            msg = "Name successfully Added"
        except:
            con.rollback()
            msg = "We can not add the name to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()


@app.route("/view")
def view():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from CRUD_for_user_info")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

@app.route("/getvalues")
def getvalues():
    return render_template("getvalues.html")
'''
@app.route("/getrecords", methods=["POST"])
def getrecords():
    msg = "msg"
    id = request.form["id"]
    with sqlite3.connect(DATABASE) as con:
        try:
            cur = con.cursor()
            cur.execute("SELECT NAME,LOCATION, EMAIL_ID FROM CRUD_for_user_info WHERE ID =?',(id,))
            user = cur.fetchone()
            print(user)
            conn.commit()
        except:
            con.rollback()
            msg = "We can not get the records from the list"
        finally:
            return render_template("success_getvalues.html", msg=msg)
            con.close()
'''
@app.route("/viewsinglerecord", methods=["POST"])
def viewsinglerecord():
    id = request.form["id"]
    con = sqlite3.connect(DATABASE)
    #con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('''SELECT NAME,LOCATION, EMAIL_ID FROM CRUD_for_user_info WHERE ID =?''',(id,))
    rows = cur.fetchone()
    print(rows)
    return render_template("viewsinglerecord.html", rows=rows)
@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/update_record", methods = ["POST"])
def updateSqliteTable():
    msg = "msg"
    id = int(request.form["id"])
    Location = request.form["location"]
    Email_id = request.form["email_id"]
    try:
        sqliteConnection = sqlite3.connect('CRUD.db')
        cursor = sqliteConnection.cursor()
        sql_update_query = """Update CRUD_for_user_info set LOCATION = ?,EMAIL_ID = ? where ID = ?"""
        data = (Location,Email_id, id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        msg = "Successfully updated"
    except sqlite3.Error as error:
        msg = "Failed to update sqlite table"
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            return render_template("update_record.html", msg=msg)

@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    
    
    with sqlite3.connect(DATABASE) as con:
        try:
            cur = con.cursor()
            cur.execute(
                'delete from CRUD_for_user_info where ID = ? ',id)
            msg = "Record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)

@app.route("/delete_all")
def logout():
    msg = "msg"
    
    with sqlite3.connect(DATABASE) as con:
        try:
           c = con.cursor()
           c.execute('DELETE FROM CRUD_for_user_info ;',);
           con.commit()
           msg = "We have delete all the files"
         
        except:
           msg = "Cant be deleted"
        finally:
           return render_template("delete_all.html", msg=msg)
           conn.close()
if __name__ == "__main__":
    app.run(debug=True)
