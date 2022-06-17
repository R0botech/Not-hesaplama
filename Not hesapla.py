kirmizi = "\u001b[31;1m"
yesil = "\u001b[32m"
sari = "\u001b[33;1m"
mavi ="\u001b[34;1m"

print(yesil + """
*********************************
    OGRENCI NOT HESAPLAMA
*********************************""")


vize1 = int(float(input(kirmizi +"lutfen vizenin birinci notunu giriniz:")))
vize2 = int(float(input(kirmizi + "lutfen vizenin ikinci notunu giriniz: ")))
final = int(float(input(kirmizi + "lutfen final notunu giriniz: ")))

a = float((vize1*30)/100) #vizenin %30 unu hesaplar
b = float((vize2*30)/100) #ikinci vizenin %30 unu hesaplar.
c = float((final*40)/100) #finalin %40 ini hesaplar.

print (mavi + "birinci vizenin %30'u :", a)
print(mavi + "ikinci vizenin %30'u :",b)
print(mavi + "finalin %40'i :",c)

notlarin_toplami = a+b+c

print(sari + "not durumu: ",notlarin_toplami)

if notlarin_toplami >= 90 and notlarin_toplami<=100:
	print(mavi + "Not Durumu:",'AA')
elif notlarin_toplami >= 85 and notlarin_toplami <90:
	print(mavi + "Not Durummu:",'BA')
elif notlarin_toplami >= 80 and notlarin_toplami < 85:
	print(mavi + "Not Durumu:",'BB')
elif notlarin_toplami >= 75 and  notlarin_toplami< 80:
	print(mavi + "Not Durumu:",'CB')
elif notlarin_toplami >= 70 and notlarin_toplami < 75:
	print(mavi + "Not Durumu:",'CC')
elif notlarin_toplami >= 65 and notlarin_toplami < 70:
	print(mavi + "Not Durumu: ",'DC')
elif notlarin_toplami >= 60 and notlarin_toplami < 65:
	print(mavi + "Not Durumu:",'DD')
elif notlarin_toplami >= 55 and notlarin_toplami <60 :
	print(mavi + "Not Durumu: ",'FD')
else :
	print(mavi + "Not Durumu: ",'FF')
			
