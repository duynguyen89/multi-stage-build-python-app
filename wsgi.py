from app import create_app
app = create_app('config.ProductionConfig')  # This should now work

if __name__ == '__main__':
    app.run()