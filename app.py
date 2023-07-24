from flask import Flask, render_template, request,session,redirect,url_for
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
    
@app.route("/login")
def login():
    return render_template('login.html')
@app.route("/login", methods=["GET","POST"])
def process_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Create a new database connection (same as before)
        # ...
        conn = create_db_connection()


        # Check user credentials in the database
        try:
            cursor = conn.cursor()
            sql = "SELECT email FROM customer WHERE email = %s AND password = %s"
            values = (email, password)
            cursor.execute(sql, values)
            user = cursor.fetchone()
            cursor.close()
            conn.close()

            if user:
                # User is authenticated, store email in session and redirect to the dashboard
                session["user_email"] = email
                return redirect(url_for("dashboard"))
            else:
                return "Invalid credentials. Please try again."

        except mysql.connector.Error as error:
            print("Error: ", error)
            return "Error occurred while processing login."

# Route for the dashboard (a simple example of an authenticated page)
@app.route("/dashboard")
def dashboard():
    user_email = session.get("user_email")
    if user_email:
        return render_template('dashbord.html')
        # return f"Welcome! User Email: {user_email}"
    else:
        return "Access denied. Please log in first."
        
if __name__ == "__main__":
    app.secret_key = "email"  # Replace with your secret key
    with app.app_context():
        conn = create_db_connection()
        cursor = conn.cursor()

        # Recreate the 'users' table with email as the primary key
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customer (
                    email VARCHAR(100) PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    password VARCHAR(100) NOT NULL,
                    address VARCHAR(200) NOT NULL,
                    user_type VARCHAR(50) NOT NULL
                )
            """)
            conn.commit()
        except mysql.connector.Error as error:
            print("Error creating 'users' table:", error)

        cursor.close()
        conn.close()

    app.run(debug=True)

