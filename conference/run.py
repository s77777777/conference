from flask import Flask


from conference import create_app
app = create_app()

if __name__ == '__main__':
    app.run()
