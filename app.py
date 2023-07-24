from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Database Configuration
db_config = {
    'host': 'localhost',  # XAMPP MySQL server is usually on localhost
    'user': 'root',       # XAMPP MySQL default username is 'root'
    'password': '',       # XAMPP MySQL default password is empty (no password)
    'database': 'laundryservice'  # Replace 'your_database_name' with your desired database name
}

# Function to create a connection to MySQL database
def create_db_connection():
    return mysql.connector.connect(**db_config)

# Route to display the index.html template
@app.route("/")
def hello_world():
    return render_template('index.html')

# Route to display the signup.html template
@app.route("/signup")
def sign():
    return render_template('signup.html')

# Route to handle the form submission for signup
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        address = request.form.get("address")
        user_type = request.form.get("user_type")

        # Create a new database connection
        conn = create_db_connection()

        # Insert user data into the database
        
        cursor = conn.cursor()
        sql = "INSERT INTO customer (name, email, password, address,user_type) VALUES (%s, %s, %s, %s,%s)"
        values = (name, email, password, address,user_type)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        return "User registered successfully!"
        

if __name__ == "__main__":
    app.run(debug=True)
