
from flask import Flask,render_template,request
import mysql as sql
app=Flask(name)

my_connection=sql.connect(
    host="localhost",
    user="root",
    password='password#123',
    database='register'
)
my_cursor= my_connection.cursor()

@app.route('/',methods=['GET'])
def homepage():
    render_template('index.html')

@app.route('/admission',methods=['GET'])
def admission():
    return render_template('admission.html')

@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/register-form',methods=['POST'])
def register_form():
    _id=request.form['_id']
    sname=request.form['sname']
    email=request.form['email']
    phone=request.form['phone']
    srank=request.form['srank']
    percentage=request.form['percentage']
    course=request.form['course']
    address=request.form['address']

    query='''
        insert into students(_id,sname,email,phone,srank,percentage,course,address)
        values(%s,%s,%s,%s,%s,%s,%s,%s);
     '''

    values=(_id,sname,email,phone,srank,percentage,course,address)
    my_cursor.execute(query,values)
    my_connection.commit()
    return 'registration completed successfully'
@app.route('/view',methods=['GET'])
def view():
    query='''
        select * from students
    '''
    my_cursor.execute(query)
    data=my_cursor.fetchall()
    return render_template('view.html',details=data)

@app.route('/update',methods=['GET'])
def update():
    return render_template('update.html')

@app.route('/update-form',methods=['POST'])
def update_form():
    sid=request.form['_id']
    field=request.form['field']
    new_value=request.form['new_value']

    query=f'''
        update students
        set {field}='{new_value}'
        where _id={sid};
    '''
    my_cursor.execute(query)
    my_connection.commit()
    return 'updated successfully'
@app.route('/delete',methods=['GET'])
def delete():
    return render_template('delete.html')

@app.route ('/delete-form',methods=['POST'])
def delete_form():
    _id=request.form['id']
    query=f'''
    delete from students
    where _id={_id}'''
    my_cursor.execute(query)
    my_connection.commit()
    return f'user {_id} is deleted'

@app.route('/query-form',methods=['POST'])
def query_form():
    sname=request.form['sname']
    email=request.form['email']
    phone=request.form['phone']
    course=request.form['course']

    query='''
        insert into form(sname,email,phone,course)
        values(%s,%s,%s,%s);'''
    values=(sname,email,phone,course)
    my_cursor.execute(query,values)
    my_connection.commit()
    return render_template('index.html')
    app.run()