from app import create_app

app = create_app()  # Factory pattern

if __name__ == '__main__':
    app.run()