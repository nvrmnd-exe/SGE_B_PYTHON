class Cotxe:
    def __init__ (self, marca, model, anyModel, color, preu):
        self.marca = marca
        self.model = model
        self.anyModel = anyModel
        self.color = color
        self.preu = preu

    
    def getmarca(self):
        return self.marca
    def setmarca(self, new_marca):
        self.marca = new_marca

    def getmodel(self):
        return self.model
    def setmodel(self, new_model):
        self.model = new_model

    def getanyModel(self):
        return self.anyModel
    def setanyModel(self, new_anyModel):
        self.anyModel = new_anyModel

    def getcolor(self):
        return self.color
    def setcolor(self, new_color):
        self.color = new_color

    def getpreu(self):
        return self.preu
    def setpreu(self, new_preu):
        self.preu = new_preu