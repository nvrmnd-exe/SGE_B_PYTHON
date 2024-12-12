class Colibri:
    def __init__(self, especie, pes, envergadura, habitat, edat):
        self.especie = especie
        self.pes = pes
        self.envergadura = envergadura
        self.habitat = habitat
        self.edat = edat

    def getespecie(self):
        return self.especie
    def setespecie(self, new_especie):
        self.especie = new_especie

    def getpes(self):
        return self.pes
    def setpes(self, new_pes):
        self.pes = new_pes

    def getenvergadura(self):
        return self.envergadura
    def setenvergadura(self, new_envergadura):
        self.envergadura = new_envergadura

    def gethabitat(self):
        return self.habitat
    def sethabitat(self, new_habitat):
        self.habitat = new_habitat

    def getedat(self):
        return self.edat
    def setedat(self, new_edat):
        self.edat = new_edat