class Num:
    def __init__(self):
        self.TF = False
        self.number = 0
        self.coord = 0

    def __int__(self, number, TF, coord):
        self.number = number
        self.TF = TF
        self.coord = coord

    def get_number(self):
        return self.number

    def get_TF(self):
        return self.TF

    def get_coord(self):
        return self.coord

    def set_number(self, a):
        self.number = a

    def set_TF(self, TF):
        self.TF = TF

    def set_coord(self, coord):
        self.coord = coord
