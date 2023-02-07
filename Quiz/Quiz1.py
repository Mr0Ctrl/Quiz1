out = str()
print("Verilen kurala gore stringleri yeniden olusturan kodu yaziniz.\nKural su sekildedir; n bir tamsayi ve str bir string olmak uzere;\nn[str] ifadesi n defa str string objesini tekrarlanmasi ile olusan\nyeni stringi olusturur.")
print("Ornek:\n\t3[a]2[bc] > aaabcbc \n\t2[abc]3[cd]ef > abcabccdcdcdef \n\t3[a2[c]] > accaccacc ")

inp = input("\t:")
#print(inp)


def Tara(veri):
    out = str()
    alan = 0
    aralik = str()
    katSayi = 1

    for i in veri:
        #print(out)
        #alanýn varlýðýný kontrol ediyor
        if i == "]":
            alan -=1
        if alan:
            aralik += i
        if i == "[":
            alan +=1

        #alan var olmamasý durumu
        if 0 == alan and i :
            out += Tara(aralik) * katSayi
            aralik = ""
            katSayi = 0
            #print(f"girdi: {i}")

            try:
                katSayi = int(i)
            except :
                if i != "]" :
                    out += i


    #print(10*"-")
    #print(aralik)
    #print(10*"-")
    return out


print("\n\t"+Tara(inp))
