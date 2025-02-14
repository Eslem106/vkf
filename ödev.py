# Sohbet edebilen ve hesap yapabilen bot

print("Merhaba! Ben bir sohbet botuyum. Yardımcı olabilir miyim?")

# Kullanıcıdan ilk mesajı al
user_input = input()

if user_input == "merhaba":
    print("Bot: Merhaba! Nasılsın?")

# Kullanıcıdan ikinci mesajı al
user_input = input()

if user_input == "nasılsın?":
    print("Bot: Ben bir botum, her zaman iyiyim! Sen nasılsın?")

# Kullanıcı hesap yapmak istediğinde
user_input = input()

if "hesap yap" in user_input or "hesap" in user_input:
    print("Bot: Tamam, sana bir hesaplama yapayım. Hangi işlemi yapmak istersin?")
    print("Bot: Örnek olarak '2 + 2' yazabilirsin.")

    hesap = input()

    # Hesaplama işlemi: +, -, *, /
    if "+" in hesap:
        sayi1, sayi2 = hesap.split("+")
        print(f"Bot: Sonuç: {int(sayi1) + int(sayi2)}")
    elif "-" in hesap:
        sayi1, sayi2 = hesap.split("-")
        print(f"Bot: Sonuç: {int(sayi1) - int(sayi2)}")
    elif "*" in hesap:
        sayi1, sayi2 = hesap.split("*")
        print(f"Bot: Sonuç: {int(sayi1) * int(sayi2)}")
    elif "/" in hesap:
        sayi1, sayi2 = hesap.split("/")
        if int(sayi2) != 0:
            print(f"Bot: Sonuç: {int(sayi1) / int(sayi2)}")
        else:
            print("Bot: Bölme işleminde sıfıra bölme hatası!")
    else:
        print("Bot: Geçersiz işlem. Lütfen tekrar deneyin.")

# Son mesaj
user_input = input()

if user_input == "hoşça kal":
    print("Bot: Hoşça kal! Görüşmek üzere.")
else:
    print("Bot: Bunu anlamadım, tekrar sorabilir misin?")