from webserver import build_app


if __name__ == '__main__':
    app = build_app()
    
    try:
        print("Running webserver")
        app.run(port=8888)
    except KeyboardInterrupt:
        print("Stopping webserver")
        app.stop()