
from myapp import app

if __name__ == '__main__':
    if not app.debug:
        import logging
        from logging.handlers import TimedRotatingFileHandler
        file_handler = TimedRotatingFileHandler("abapi.log",when="D", backupCount=10)
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)

    app.debug = app.config['DEBUG']
    app.run()


