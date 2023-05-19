from website import create_app

app = create_app()

#ensures web server only runs if the file is ran directly
if __name__ == '__main__':
    app.run(debug=True)
    #^ starts up web server
    #debug = true, any changes to python code happen live.
