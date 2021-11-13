from root import process_app
app = process_app()
if __name__ == '__main__':
    
    app.run(port=80, host='localhost', debug=True)
