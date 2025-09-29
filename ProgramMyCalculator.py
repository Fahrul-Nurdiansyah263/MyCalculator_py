print("                                             SELAMAT DATANG DI MYCALCULATOR")
print("===================================================================================================================")
print("\nPilih option")
print("1. Bangun Datar")
print("2. Bangun Ruang")
print("3. Calculator")

option=int(input("Silahkan pilih option : "))

if option==1:

    def persegi():
        print("Hitung  persegi ready")
        sisi = float(input("Masukkan sisi : "))
        luas = (sisi * sisi)
        keliling = (4 * sisi)
        print("Rumus:\nLuas = sisi x sisi\nKeliling = 4 x sisi")
        print("================Hasilnya===================")
        print("keliling persegi berikut adalah :",keliling)
        print("Luas persegi berikut adalah : ",luas, "\n")

    def persegipanjang():
        print("Hitung persegi panjang ready")
        panjang = float(input("Masukkan panjang :"))
        lebar = float(input("Masukkan lebar : "))
        luas = (panjang*lebar)
        keliling = 2*(panjang+lebar)
        print("Rumus\nLuas = Panjang x Lebar\nKeliling = 2 x (Panjang x Lebar)")
        print("=================Hasilnya====================")
        print("Keliling persegi panjang berikut adalah :",keliling)
        print("Luas persegi panjang berikut adalah : ",luas, "\n")    

    def segitiga():
        print("Hitung segitiga ready")
        alas = float(input("Masukkan alas :"))
        tinggi =float(input("Masukkan tinggi :"))
        sisi = float(input("Masukkan sisi :"))
        keliling = 3 * sisi
        luas = 0.5 * (alas * tinggi)
        print("Rumus\nKeliling = 3 x sisi\nLuas = 0.5 x (alas x tinggi)")
        print("==================Hasilnya=====================")
        print("Keliling segitiga berikut adalah :",keliling)
        print("luas segitiga berikut adalah: ", luas, "\n")  

    def jajargenjang():
        print("Hitung jajar genjang ready")
        a = float(input("Masukkan alas :"))
        t =float(input("Masukkan tinggi :"))
        b = float(input("Masukkan sisi miring :"))
        keliling = 2*(a+b)
        luas = (a * t)
        print("Rumus\nKeliling = 2 x (alas + sisi miring)\nLuas = (alas x tinggi) ")
        print("====================Hasilnya=====================")
        print("Keliling jajar genjang berikut adalah :",keliling)
        print("Luas jajar genjang berikut adalah :",luas, "\n")  

    def trapesium():
        print("Hitung trapesium ready")
        jumlah_sisi_sejajar = float(input("Masukkan jumlah sisi sejajar :"))
        tinggi = float(input("Masukan tinggi :"))
        AB = float(input("Masukkan nilai AB :"))
        BC = float(input("Masukkan nilai BC :"))
        CD = float(input("Masukkan nilai CD :"))
        DA = float(input("Masukkan nilai DA :"))
        keliling = (AB+BC+CD+DA)
        luas = (jumlah_sisi_sejajar * tinggi)/2
        print("Rumus\nKeliling = nilai AB + nilai BC + nilai CD + nilai DA\nLuas = (Jumlah sisi sejajar x tinggi) : 2")
        print("======================Hasilnya=======================")
        print("Keliling trapesium berikut adalah :",keliling)
        print("Luas trapesium berikut adalah :",luas, "\n")          

    def layanglayang():
        print("Hitung layang layang ready")
        diagonal1 = float(input("Masukkan diagonal 1 :"))
        diagonal2 = float(input("Masukkan diagonal 2 :"))
        a = float(input("Masukkan nilai a :"))
        b = float(input("Masukkan nilai b :"))
        keliling = 2*(a+b)
        luas = (diagonal1 * diagonal2)/2
        print("Rumus\nKeliling = 2 x (nilai a + b)\nLuas = (diagonal 1 x diagonal 2) : 2")
        print("========================Hasilnya=======================")
        print("Keliling layang layang berikut adalah :",keliling)
        print("Luas layang layang berikut adalah :",luas, )

    def belahketupat():
        print("Hitung luas belah ketupat ready")
        diagonal1 = float(input("Masukkan diagonal 1 :"))
        diagonal2 = float(input("Masukkan diagonal 2 :"))
        s = float(input("Masukkan sisi :"))
        keliling = 4*s
        luas = (diagonal1 * diagonal2)/2
        print("Rumus\nKeliling = 4 x sisi\nLuas = (diagonal 1 x diagonal 2) : 2")
        print("=========================Hasilnya=========================")
        print("Keliling belah ketupat berikut adalah :",keliling)
        print("Luas belah ketupat berikut adalah :",luas)

    while True:
        userInput = int(input("\n\npilih bangun datar yang akan dihitung:  \n\n1.persegi\n2.persegi panjang\n3.segitiga\n4.jajar genjang\n5.trapesium\n6.layang layang\n7.belah ketupat\n0.keluar program\n\nmasukkan angka :"))

        if(userInput == 1):
            persegi()  
        elif(userInput == 2):
            persegipanjang()
        elif(userInput == 3):
            segitiga()          
        elif(userInput == 4):
            jajargenjang()
        elif(userInput == 5):
            trapesium()
        elif(userInput == 6):
            layanglayang()
        elif(userInput == 7):
            belahketupat()                       
        else:
            print("Terima Kasih telah menggunakan MYCALCULATOR:)")
            break       

        pilihan = input("Apakah anda ingin menghitung bangun datar lain?[y/n]")

        if pilihan == 'y':
            userInput
        else:
            print("Terima Kasih telah menggunakan MYCALCULATOR:)")
            break        
elif option==2: 

        
    def kubus():
        print("Hitung kubus ready")
        sisi = float(input("Masukkan sisi :"))
        luas = 6 * sisi
        keliling = 12 * sisi
        volume = sisi * sisi * sisi
        print("Rumus\nLuas = 6 x sisi\nKeliling = 12 x sisi\nVolume = sisi x sisi x sisi")
        print("=====================Hasilnya=====================")
        print("Luas kubus berikut adalah        =",luas)
        print("Keliling kubus berikut adalah    =",keliling)
        print("Volume kubus berikut adalah      =",volume)

    def balok():
        print("Hitung balok ready")
        p = float(input("Masukkan panjang :"))
        l = float(input("Masukkan lebar :"))
        t = float(input("Masukkan tinggi :"))
        luas = 2 * (p*l) + 2 * (p*t) + 2 * (l*t)
        keliling = 4 * (p+l+t)
        volume = p * l * t
        print("Rumus\nLuas = 2 x (panjang x lebar) + 2 x (panjang x tinggi) + 2 x (lebar x tinggi)\nKeliling = 4 x (panjang + lebar + tinggi)\nVolume = panjang x luas x tinggi")
        print("=======================Hasilnya=====================")
        print("Luas balok berikut adalah        =",luas)
        print("Keliling balok berikut adalah    =",keliling)
        print("Volume balok berikut adalah      =",volume)
            
    def tabung():
        print("Hitung tabung ready")
        r = float(input("Masukkan jari jari :"))
        t = float(input("Masukkan tinggi silinder tabung :"))
        luas_selimut_tabung = 2*22/7*r*t
        luas_permukaan_tabung = (2*22/7*r*t)+2*22/7*(r**2)
        volume = 22/7*r*r*t
        print("Rumus\nLuas selimut tabung = 2 x 22 : 7 x jari-jari x tinggi tabung\nLuas permukaan tabung = (2 x 22 : 7 x jari-jari x tinggi tabung) + 2 x 22 : 7 x (jari-jari² x 2)\nVolume = 22/7 x r x r x t")
        print("=========================Hasilnya======================")
        print("Luas selimut tabung berikut adalah :",luas_selimut_tabung)
        print("Luas permukaan tabung berikut adalah :",luas_permukaan_tabung)
        print("Volume tabung berikut adalah :",volume)

    def kerucut():
        print("Hitung kerucut ready")
        r = float(input("Masukkan jari jari alas kerucut :"))
        p = float(input("Masukkan panjang garis pelukis kerucut :"))
        t = float(input("Masukkan tinggi kerucut :"))
        luas_selimut = 3.14*r*p 
        luas_permukaan =3.14*r*p+3.14*(r**2)
        volume = 0,333*22/7*r*r*t
        print("Rumus\nLuas selimut = 3,14 x jari-jari x panjang garis pelukis\nLuas permukaan = 𝜋.r (r+s)\nVolume = ⅓ 𝜋.r².t")
        print("==========================Hasilnya========================")
        print("Luas selimut kerucut berikut adalah :",luas_selimut)  
        print("Luas permukaan kerucut berikut adalah :",luas_permukaan)
        print("Volume kerucut berikut adalah :",volume)

    def bola():
        print("Hitung bola ready")
        phi = 3.14
        r = float(input("Masukkan jari jari bola :"))
        luas = 4*(phi*r*r)
        volume = 4/3*phi*r*r*r 
        print("Rumus\nLuas = 4 x π x r²\nVolume = (4/3) x π x r3")
        print("===========================Hasilnya============================")
        print("Luas bola berikut adalah   :",luas)
        print("Volume bola berikut adalah   :",volume)  

    def prisma_segitiga():
        print("Hitung prisma segitiga ready")
        keliling = float(input("Masukkan keliling prisma :"))
        tp = float(input("Masukkan tinggi prisma :"))
        ts = float(input("Masukkan tinggi segitiga :"))
        als = float(input("Masukkan alas segitiga :"))
        luas_selimut = keliling*tp
        luas_permukaan = keliling*tp +(als*ts)
        volume = 1/2*als*ts*tp 
        print("Rumus\nLuas selimut = Keliling x Tinggi prisma\nLuas permukaan = Keliling x Tinggi prisma + (alas x tinggi segitiga)\nVolume = (½ x alas x tinggi segitiga) x Tinggi prisma")
        print("==========================Hasilnya==============================")
        print("Luas selimut prisma segitiga berikut adalah   :",luas_selimut)
        print("Luas permukaan prisma segitiga berikut adalah   :",luas_permukaan)
        print("Volume prisma segitiga berikut adalah   :",volume)

    def limas_segitiga():
        print("Hitung limas segitiga ready")
        ls = float(input("Masukkan luas segitiga :"))
        la = float(input("Masukkan luas alas :"))
        t = float(input("Masukkan tinggi segitiga :"))
        luas = 0.5 * la * t
        volume = 1/3*la*t
        print("Rumus\nLuas = 1/2 x alas x tinggi\nVolume = 1/3 x luas alas x Tinggi")
        print("===========================Hasilnya===========================")
        print("Luas limas segitiga berikut adalah    :",luas)
        print("Volume limas segitiga berikut adalah    :",volume)

    def limas_segiempat():
        print("Hitung limas segiempat ready")
        sa = float(input("Masukkan sisi alas :"))
        tinggi = float(input("Masukkan tinggi sisi tegak :"))
        tl = float(input("Masukkan tinggi limas :"))
        luas = (sa*sa)+(0.5*sa*tinggi)
        volume = (0.333*sa*sa)*tl 
        print("Rumus\nLuas = (sisi alas x sisi alas) + (1/2 x sisi alas x tinggi sisi tegak)\nVolume = (1/3 x sisi alas x sisi alas) x tinggi limas")
        print("============================Hasilnya===========================")
        print("Luas limas segiempat berikut adalah   :",luas)
        print("Volume limas segiempat berikut adalah   :",volume)   

    while True:
        userInput = int(input("\n\npilih bangun ruang yang akan dihitung  :  \n\n1.kubus\n2.balok\n3.tabung\n4.kerucut\n5.bola\n6.prisma segitiga\n7.limas segitiga\n8.limas segiempat \n0.keluar program\n\nmasukkan angka :"))

        if(userInput == 1):
            kubus() 
        elif(userInput == 2):
            balok()  
        elif(userInput == 3):
            tabung()         
        elif(userInput == 4):
            kerucut()
        elif(userInput == 5):
            bola() 
        elif(userInput == 6):
            prisma_segitiga()
        elif(userInput == 7):
            limas_segitiga() 
        elif(userInput == 8):
            limas_segiempat()              
        else:
            print("Terima Kasih telah menggunakan MYCALCULATOR:)")
            break  

        pilihan = input("Apakah anda ingin menghitung bangun ruang lain?[y/n]")

        if pilihan == 'y':
            userInput 
        else:
            print("Terima Kasih telah menggunakan MYCALCULATOR:)")
            break    

elif option==3: 

    def penjumlahan() : 
        def penjumlahan_2_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            print ("Hasil = ", (a+b) )

        def penjumlahan_3_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            print ("Hasil = ", (a+b+c) )

        def penjumlahan_4_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            print ("Hasil = ", (a+b+c+d) )

        def penjumlahan_5_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            print ("Hasil = ", (a+b+c+d+e) )

        def penjumlahan_6_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            print ("Hasil = ", (a+b+c+d+e+f) )

        def penjumlahan_7_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            print ("Hasil = ", (a+b+c+d+e+f+g) )

        def penjumlahan_8_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            h = float(input("Bilangan kedelapan    : "))
            print ("Hasil = ", (a+b+c+d+e+f+g+h) )

        def penjumlahan_9_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            h = float(input("Bilangan kedelapan    : "))
            i = float(input("Bilangan kesembilan    : "))
            print ("Hasil = ", (a+b+c+d+e+f+g+h+i) )

        def penjumlahan_10_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            h = float(input("Bilangan kedelapan    : "))
            i = float(input("Bilangan kesembilan    : "))
            j = float(input("Bilangan Kesepuluh    : "))
            print ("Hasil = ", (a+b+c+d+e+f+g+h+i+j) )

        while True :
            penjumlahan = int((input("Pilih penjumlahan\n1.penjumlahan dua bilangan\n2.penjumlahan tiga bilangan\n3.penjumlahan empat bilangan\n4.penjumlahan lima bilangan\n5.penjumlahan enam bilangan\n6.penjumlahan tujuh bilangan\n7.penjumlahan delapan bilangan\n8.penjumlahan sembilan bilangan\n9.penjumlahan sepuluh bilangan\n0.keluar program\nMasukan angka : ")))

            if penjumlahan==1:
                penjumlahan_2_bilangan()
            elif penjumlahan==2:
                penjumlahan_3_bilangan()
            elif penjumlahan==3:
                penjumlahan_4_bilangan()
            elif penjumlahan==4:
                penjumlahan_5_bilangan()
            elif penjumlahan==5:
                penjumlahan_6_bilangan()
            elif penjumlahan==6:
                penjumlahan_7_bilangan()
            elif penjumlahan==7:
                penjumlahan_8_bilangan()    
            elif penjumlahan==8:
                penjumlahan_9_bilangan()
            elif penjumlahan==9:
                penjumlahan_10_bilangan()
            else:
                break    

            pilihan = input("Apakah anda ingin mengitung kembali?[y/n]")

            if pilihan == 'y':
                penjumlahan
            else:
                break 

    def pengurangan () :
        def pengurangan_2_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            print ("Hasil = ", (a-b) )

        def pengurangan_3_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            print ("Hasil = ", (a-b-c) )

        def pengurangan_4_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            print ("Hasil = ", (a-b-c-d) )

        def pengurangan_5_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            print ("Hasil = ", (a-b-c-d-e) )

        def pengurangan_6_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            print ("Hasil = ", (a-b-c-d-e-f) )

        def pengurangan_7_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            print ("Hasil = ", (a-b-c-d-e-f-g) )

        def pengurangan_8_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            h = float(input("Bilangan kedelapan    : "))
            print ("Hasil = ", (a-b-c-d-e-f-g-h) )

        def pengurangan_9_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            h = float(input("Bilangan kedelapan    : "))
            i = float(input("Bilangan kesembilan    : "))
            print ("Hasil = ", (a-b-c-d-e-f-g-h-i) )

        def pengurangan_10_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            h = float(input("Bilangan kedelapan    : "))
            i = float(input("Bilangan kesembilan    : "))
            j = float(input("Bilangan Kesepuluh    : "))
            print ("Hasil = ", (a-b-c-d-e-f-g-h-i-j) )

        while True :
            pengurangan = int((input("Pilih pengurangan\n1.pengurangan dua bilangan\n2.pengurangan tiga bilangan\n3.pengurangan empat bilangan\n4.pengurangan lima bilangan\n5.pengurangan enam bilangan\n6.pengurangan tujuh bilangan\n7.pengurangan delapan bilangan\n8.pengurangan sembilan bilangan\n9.pengurangan sepuluh bilangan\n0.keluar program\nMasukan angka : ")))

            if pengurangan==1:
                pengurangan_2_bilangan()
            elif pengurangan==2:
                pengurangan_3_bilangan()
            elif pengurangan==3:
                pengurangan_4_bilangan()
            elif pengurangan==4:
                pengurangan_5_bilangan()
            elif pengurangan==5:
                pengurangan_6_bilangan()
            elif pengurangan==6:
                pengurangan_7_bilangan()
            elif pengurangan==7:
                pengurangan_8_bilangan()    
            elif pengurangan==8:
                pengurangan_9_bilangan()
            elif pengurangan==9:
                pengurangan_10_bilangan()
            else:
                break   
        
            pilihan = input("Apakah anda ingin menghitung kembali?[y/n]")

            if pilihan == 'y':
                pengurangan 
            else :
                break           

    def perkalian():
        def perkalian_2_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            print ("Hasil = ", (a*b) )

        def perkalian_3_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            print ("Hasil = ", (a*b*c) )

        def perkalian_4_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            print ("Hasil = ", (a*b*c*d) )

        def perkalian_5_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            print ("Hasil = ", (a*b*c*d*e) )

        def perkalian_6_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            print ("Hasil = ", (a*b*c*d*e*f) )

        def perkalian_7_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            print ("Hasil = ", (a*b*c*d*e*f*g) )

        def perkalian_8_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            h = float(input("Bilangan kedelapan    : "))
            print ("Hasil = ", (a*b*c*d*e*f*g*h) )

        def perkalian_9_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            h = float(input("Bilangan kedelapan    : "))
            i = float(input("Bilangan kesembilan    : "))
            print ("Hasil = ", (a*b*c*d*e*f*g*h*i) )

        def perkalian_10_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            h = float(input("Bilangan kedelapan    : "))
            i = float(input("Bilangan kesembilan    : "))
            j = float(input("Bilangan Kesepuluh    : "))
            print ("Hasil = ", (a*b*c*d*e*f*g*h*i*j) )

        while True :
            perkalian = int((input("Pilih perkalian\n1.Perkalian dua bilangan\n2.Perkalian tiga bilangan\n3.Perkalian empat bilangan\n4.Perkalian lima bilangan\n5.Perkalian enam bilangan\n6.Perkalian tujuh bilangan\n7.Perkalian delapan bilangan\n8.Perkalian sembilan bilangan\n9.Perkalian sepuluh bilangan\n0.keluar program\nMasukan angka : ")))

            if perkalian==1:
                perkalian_2_bilangan()
            elif perkalian==2:
                perkalian_3_bilangan()
            elif perkalian==3:
                perkalian_4_bilangan()
            elif perkalian==4:
                perkalian_5_bilangan()
            elif perkalian==5:
                perkalian_6_bilangan()
            elif perkalian==6:
                perkalian_7_bilangan()
            elif perkalian==7:
                perkalian_8_bilangan()    
            elif perkalian==8:
                perkalian_9_bilangan()
            elif perkalian==9:
                perkalian_10_bilangan()
            else:
                break   

            pilihan = input("Apakah anda ingin menghitung kembali?[y/n]") 

            if pilihan == 'y':
                perkalian 
            else:
                break 

    def pembagian() :
        def pembagian_2_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            print ("Hasil = ", (a/b))

        def pembagian_3_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            print ("Hasil = ", (a/b/c))

        def pembagian_4_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            print ("Hasil = ", (a/b/c/d) )

        def pembagian_5_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            print ("Hasil = ", (a/b/c/d/e) )

        def pembagian_6_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            print ("Hasil = ", (a/b/c/d/e/f) )

        def pembagian_7_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            print ("Hasil = ", (a/b/c/d/e/f/g) )

        def pembagian_8_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            h = float(input("Bilangan kedelapan    : "))
            print ("Hasil = ", (a/b/c/d/e/f/g/h) )

        def pembagian_9_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            h = float(input("Bilangan kedelapan    : "))
            i = float(input("Bilangan kesembilan    : "))
            print ("Hasil = ", (a/b/c/d/e/f/g/h/i) )

        def pembagian_10_bilangan():
            a = float(input("Bilangan Pertama   : "))
            b = float(input("Bilangan Kedua     : "))
            c = float(input("Bilangan Ketiga    : "))
            d = float(input("Bilangan keempat    : "))
            e = float(input("Bilangan kelima    : "))
            f = float(input("Bilangan keenam    : "))
            g = float(input("Bilangan ketujuh    : "))
            h = float(input("Bilangan kedelapan    : "))
            i = float(input("Bilangan kesembilan    : "))
            j = float(input("Bilangan Kesepuluh    : "))
            print ("Hasil = ", (a/b/c/d/e/f/g/h/i/j) )
                                       

        while True :
            pembagian = int((input("Pilih pembagian\n1.Pembagian dua bilangan\n2.Pembagian tiga bilangan\n3.Pembagian empat bilangan\n4.Pembagian lima bilangan\n5.Pembagian enam bilangan\n6.Pembagian tujuh bilangan\n7.Pembagian delapan bilangan\n8.Pembagian sembilan bilangan\n9.Pembagian sepuluh bilangan\n0.keluar program\nMasukan angka : ")))

            if pembagian==1:
                pembagian_2_bilangan()
            elif pembagian==2:
                pembagian_3_bilangan()
            elif pembagian==3:
                pembagian_4_bilangan()
            elif pembagian==4:
                pembagian_5_bilangan()
            elif pembagian==5:
                pembagian_6_bilangan()    
            elif pembagian==6:
                pembagian_7_bilangan()
            elif pembagian==7:
                pembagian_8_bilangan()
            elif pembagian==8:
                pembagian_9_bilangan()
            elif pembagian==9:
                pembagian_10_bilangan()
            else:
                break

            pilihan = input("Apakah anda ingin menghitung kembali?[y/n]")

            if pilihan == 'y':
                pembagian
            else:
                break    

    def hitung_kecepatan():
        print("hitung kecepatan ready!")
        jarak = float(input("masukan jarak(m) : "))
        waktu = float(input("masukan waktu(s): "))
        kecepatan = jarak / waktu
        print("Rumus = jarak : waktu")
        print("kecepatan: ", kecepatan, "\n")

    def hitung_jarak():
        print("hitung jarak ready!")
        kecepatan = float(input("masukan kecepatan(m/s) : "))
        waktu = float(input("masukan waktu(s) : "))
        jarak = kecepatan * waktu
        print("Rumus = kecepatan x waktu")
        print("jarak: ", jarak, "\n")

    def hitung_waktu():
        print("hitung waktu ready!")
        kecepatan = float(input("masukan kecepatan(m/s) : "))
        jarak = float(input("masukan jarak(m) : "))
        waktu = kecepatan / jarak
        print("Rumus = kecepatan : jarak")
        print("waktu: ", waktu, "\n")

    while True:
        userInput = int (input("\n\nPilih rumus yang akan dipakai :   \n\n1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian\n5.hitung kecepatan\n6.hitung jarak\n7.hitung waktu\n0.keluar program\n\nmasukkan nomor :"))

        if(userInput == 1):
            penjumlahan()
        elif(userInput == 2):
            pengurangan()
        elif(userInput == 3):
            perkalian()
        elif(userInput == 4):
            pembagian()
        elif(userInput == 5):
            hitung_jarak()
        elif(userInput == 6):
            hitung_kecepatan()
        elif(userInput == 7):
            hitung_waktu()                  
        else:
            print("Terima Kasih telah menggunakan MYCALCULATOR:)")
            break

        pilihan = input("Apakah anda ingin menghitung dengan rumus yang lain?[y/n]")

        if pilihan == 'y':
            userInput
        else:
            print("Terima Kasih telah menggunakan MYCALCULATOR:)")
            break
else:
    print("Input tidak diketahui")