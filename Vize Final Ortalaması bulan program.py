# Vize Final Ortalaması bulan program
vize=int(input("Vize Notunuzu Giriniz: "))
final=int(input("Final Notunuzu Giriniz: "))

not_ortalamasi=(vize*0.4)+(final*0.6)
print("Ders Ortalamanız: ",not_ortalamasi)
if(not_ortalamasi>=50):
    print("Geçtiniz!")
elif(not_ortalamasi<50):
    print("Kaldın :(")