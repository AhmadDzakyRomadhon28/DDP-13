from Animal import Animal

# setiap class child itu memiliki 2 method dan properti
class Amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, alat_bernafas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.alat_bernafas = alat_bernafas
        
    def info_Amphibi(self):
        super().info_animal(),
        print("Jenis air \t\t : ", self.jenis_air,
              "\nBernapas \t\t : ", self.alat_bernafas)   
        
amphibi1 = Amphibi("katak", "Berudu", "2 Alam", "Bertelur", "Air Rawa", "Kulit")
amphibi2 = Amphibi("Salamander", "Jangkrik", "2 Alam", "Bertelur", "Air Jernih", "Kulit")
amphibi3 = Amphibi("kadal", "ulat", "2 Alam", "Bertelur", "Air Rawa", "Kulit")
amphibi1.info_Amphibi()
amphibi2.info_Amphibi()
amphibi3.info_Amphibi()