# Marble Class
class marble:
    locType = "play"
    index   = 0
    color   = "white"
    full    = False

    # Init
    def __init__(self, locType, index, color, full):
        self.locType = locType # Should be one of: home, play, base
        self.index   = index
        self.color   = color
        self.full    = full # Boolean

    # Setters
    def set_locType(self, new_locType):
        self.locType = new_locType
    def set_index(self, new_index):
        self.index = new_index
    def set_color(self, new_color):
        self.color = new_color
    def set_full(self, new_full):
        self.full = new_full

    # Getters
    def get_locType(self):
        return self.locType
    def get_index(self):
        return self.index
    def get_color(self):
        return self.color
    def get_full(self):
        return self.full
