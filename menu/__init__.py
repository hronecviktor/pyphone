class MenuException(Exception):
    pass


class Menu(object):
    items = []

    def __init__(self, lcd):
        self.lcd = lcd
        self.items = []

    def __str__(self):
        return "<Menu Object: [{}]>".format([str(m_item for m_item in self.items)])

    def item_add(self, item):
        if not isinstance(item, MenuItem):
            raise MenuException("Item to be added must be of class 'menu_item'")

        self.items.append(item)

    def next(self):
        pass

    def previous(self):
        pass


class MenuItem(object):
    def __init__(self, text, fun, bitmap = None):
        self.text = text
        self.fun = fun

    def __str__(self):
        return "<Menu Item: '{}'>".format(self.name)

    def bit_map(self):
        pass
