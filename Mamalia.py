from Animal import Animal


class Mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, ukuran_tubuh, jenis_kulit):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_kulit = jenis_kulit

        
    def info_Mamalia(self):
        super().info_animal(),
        print("Ukuran Tubuh \t\t : ", self.ukuran_tubuh,
              "\nBernapas \t\t : ", self.jenis_kulit)   
        
Mamalia1 = Mamalia("Lumba-Lumba", "Ikan", "Air", "Melahirkan", "Sedang", "Lembut")
Mamalia2 = Mamalia("Sapi", "Rumput", "Daratan", "Melahirkan", "Besar", "Lembut")
Mamalia3 = Mamalia("Beruang Kutub", "Madu", "Es", "Melahirkan", "Besar", "Halus")
Mamalia1.info_Mamalia()
Mamalia2.info_Mamalia()
Mamalia3.info_Mamalia()