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
# service 
# @app.route("/service", methods=["GET","POST"])
# def service():
#     if request.method == "POST":
      
#         business_name = request.form.get("business_name")
#         service_1 = request.form.get("service_1")
#         service_1_price = request.form.get("service_1_price")
#         service_2 = request.form.get("service_2")
#         service_2_price = request.form.get("service_2_price")
#         service_3 = request.form.get("service_3")
#         service_3_price = request.form.get("service_3_price")

#         # Create a new database connection
#         conn = create_db_connection()

#         # Insert user data into the database
        
#         cursor = conn.cursor()
#         sql = "INSERT INTO service (business_name,service_1,service_1_price,service_2, service_2_price,service_3,service_3_price) VALUES (%s, %s, %s, %s,%s,%s,%s)"
#         values=(business_name,service_1,service_1_price,service_2,service_2_price,service_3,service_3_price)
#         cursor.execute(sql, values)
#         conn.commit()
#         cursor.close()
#         conn.close()
#         return "User registered successfully!"
# end service

    
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
            sql = "SELECT email,user_type FROM customer WHERE email = %s AND password = %s"
            values = (email, password)
            cursor.execute(sql, values)
            user = cursor.fetchone()
            cursor.close()
            conn.close()

            if user:
                # User is authenticated, store email in session and redirect to the dashboard
                session["user_email"] = user[0]
                session["user_type"] = user[1]
                if user[1] == "Delivery Man":
                    return redirect(url_for("dashbord"))
                elif user[1] == "Customer":
                    return redirect(url_for("customer"))
                else:
                    return redirect(url_for("service"))
            else:
                return "Invalid credentials. Please try again."

        except mysql.connector.Error as error:
            print("Error: ", error)
            return "Error occurred while processing login."

# Route for the dashboard (a simple example of an authenticated page)
@app.route("/dashbord")
def dashbord():
    user_email = session.get("user_email")
    if user_email:
        return render_template('dashbord.html')
        # return f"Welcome! User Email: {user_email}"
    else:
        return "Access denied. Please log in first."
    
@app.route("/customer")
def customer():
    user_email = session.get("user_email")
    if user_email:
        return render_template('customer.html')
        # return f"Welcome! User Email: {user_email}"
    else:
        return "Access denied. Please log in first."

@app.route("/service", methods=["GET","POST"])
def service():
    user_email = session.get("user_email")
    if user_email:

  

        if request.method == "POST":
            email=session["user_email"]
            business_name = request.form.get("business_name")
            service_1 = request.form.get("service_1")
            service_1_price = request.form.get("service_1_price")
            service_2 = request.form.get("service_2")
            service_2_price = request.form.get("service_2_price")
            service_3 = request.form.get("service_3")
            service_3_price = request.form.get("service_3_price")

            # Create a new database connection
            conn = create_db_connection()

            # Insert user data into the database
            
            cursor = conn.cursor()
            sql = "INSERT INTO service (business_name,service_1,service_1_price,service_2, service_2_price,service_3,service_3_price) VALUES (%s, %s, %s, %s,%s,%s,%s)"
            values=(business_name,service_1,service_1_price,service_2,service_2_price,service_3,service_3_price)
            cursor.execute(sql, values)
            conn.commit()
            cursor.close()
            conn.close()
        service_data=fetch_data_from_db()
            
        return render_template('service.html',service_data=service_data)
    else:
        return "Access denied. Please log in first."

#

def fetch_data_from_db():
    conn = create_db_connection()
    cursor = conn.cursor()

    try:
        # Fetch all data from the 'service' table
        cursor.execute("SELECT * FROM service")
        data = cursor.fetchall()

        cursor.close()
        conn.close()
        return data

    except mysql.connector.Error as error:
        print("Error fetching data from the database:", error)
        return None

# 
def create_db_connection():
    # Replace these with your actual database credentials
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'laundryservice',
        'auth_plugin': 'mysql_native_password'
    }

    conn = mysql.connector.connect(**config)
    return conn
def fetch_data_from_db():
    conn = create_db_connection()
    cursor = conn.cursor()

    try:
        # Example query to fetch all data from the 'users' table
        cursor.execute("SELECT * FROM service")
        data = cursor.fetchall()
        # print(data)

       

        cursor.close()
        conn.close()
        # render_template(service.html)
        return data
        # return redirect(url_for("display_service_data"))

    except mysql.connector.Error as error:
        print("Error fetching data from the database:", error)
        return None



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




