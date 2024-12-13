from Animal import Animal

class Carnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, alat_bernafas, ukuran_badan):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.alat_bernafas = alat_bernafas
        self.ukuran_badan = ukuran_badan
        
    def info_Carnivora(self):
        super().info_animal(),
        print("Bernapas \t\t : ", self.alat_bernafas,
              "\nUkuran Badan \t\t : ", self.ukuran_badan,)
        
carnivora1 = Carnivora("Macan Tutul", "Daging", "Daratan", "Melahirkan", "Paru-Paru", "Lumayan Gede")
carnivora2 = Carnivora("Anjing", "Tulang", "Daratan", "Melahirkan", "Paru-Paru", "Sedang")
carnivora3 = Carnivora("Paus Orca", "Ikan", "Air", "Melahirkan", "Paru-Paru", "Sangat Gede")
carnivora1.info_Carnivora()
carnivora2.info_Carnivora()
carnivora3.info_Carnivora()