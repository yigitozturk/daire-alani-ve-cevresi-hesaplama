def hosgeldin():
    print("""
Daire hesaplayıcısına hoşgeldin!
""")

hosgeldin()

def hesaplama():
    operation = input("""
Yapmak istediğin işlemi komut satırına yaz;
Daire alanı için ALAN
Daire çevresi için ÇEVRE

""")

    pi = float(input("Pi sayısını yazınız: "))
    yaricap = float(input("Yarıçapı yazınız: "))
    capkare = (yaricap**2)

    if operation == 'ALAN':
        print("{} * {}".format(pi,capkare))
        print(pi*capkare)
        
    elif operation == 'ÇEVRE':
        print("2 * {} * {}".format(pi,yaricap))
        print(2*pi*yaricap)
    else:
        print("")
        print("Yanlış bir komut girdiniz lütfen doğru yazınız.")
        
    tekrar()

def tekrar():
    tekraret = input(""" 
Tekrar hesaplama yapmak istiyormusun?
Lütfen yapmak istiyor isen E
Yapmamak istiyor isen H yaz.

""")

    if tekraret.upper() == 'E':
        hesaplama()
    elif tekraret.upper() == 'H':
        print("Daha sonra görüşürüz...")
    else:
        tekrar()
        
        
hesaplama()
