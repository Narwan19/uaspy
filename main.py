from core.baseapp import BaseApp

class MainApp(BaseApp):
     def __init__(self):
        self.books = []
        self.InputBook = []
        self.ViewBook = []
        BaseApp.__init__(self)


if __name__ == "__main__":
    app = MainApp()
    app.run()