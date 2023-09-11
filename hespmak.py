print("""Hesap makinesine hoş geldiniz.
      Lütfen yapmak istediğiniz işlemi seçin
      Toplama işlemi için 1'e basın
      Çıkarma işlemi için 2'e basın
      Çarpma işlemi için 3'e basın
      Bölme işlemi için 4'e basın
      """)
islem=int(input("yapacağınız işlemi seçin:"))
if islem==1:
    s1=int(input("Lütfen bir sayı girin:"))
    s2=int(input("lütfen bir sayı girin:"))
    print(f"işleminizin sonucu {s1+s2} dir",s1+s2)
elif islem==2:
    s1=int(input("lütfen bir sayı girin:"))
    s2=int(input("lütfen bir sayı girin:"))
    print(f"işleminizin sonucu {s1-s2} dir",s1-s2)
elif islem==3:
    s1=int(input("lütfen bir sayı girin:"))
    s2=int(input("lütfen bir sayı girin:"))
    print(f"işleminizin sonucu {s1*s2} dir",s1*s2)
elif islem==4:
    s1=int(input("lütfen bir sayı girin:"))
    s2=int(input("lütfen bir sayı girin:"))
    print(f"işleminizin sonucu {s1/s2} dir",s1/s2)
else:
    print("hatalı işlem seçimi yaptınız!!!")