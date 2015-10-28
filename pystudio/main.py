
import enaml
from enaml.qt.qt_application import QtApplication
from enaml.qt.qt_factories import QT_FACTORIES
from enaml.application import ProxyResolver

# stub for now
CUSTOM_FACTORIES = {}

class App(QtApplication):
    def __init__(self):
        super(App, self).__init__()
        factories = dict(QT_FACTORIES)
        factories.update(CUSTOM_FACTORIES)
        self.resolver = ProxyResolver(factories=factories)


def main():
    app = App()

    with enaml.imports():
        from pystudio import Main

    view = Main()
    view.show()

    app.start()


if __name__ == "__main__":
    main()
