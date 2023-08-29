from website import create_app
if __name__ == '__main__':
    try:
        app = create_app() 
        app = app.run(debug=True)
    except Exception as e:
        print("Error: ", e)
        