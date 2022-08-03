def kody_pocztowe(pierwsza_wartość,druga_wartość):
    """
    Pobiera zakres kodów pocztowych i 
    zwraca tablicę kodów pocztowych znadujących się w podanym zakresie
    """
    
    #konwertowanie na int
    poczatek = list(pierwsza_wartość)
    koniec = list(druga_wartość)
    
    poczatek1 = poczatek[0] + poczatek[1]
    poczatek1 = int(poczatek1)

    poczatek2 = poczatek[3] + poczatek[4] + poczatek[5]
    poczatek2 = int(poczatek2)
    
    koniec1 = koniec[0] + koniec[1]
    koniec1 = int(koniec1)

    koniec2 = koniec[3] + koniec[4] + koniec[5]
    koniec2 = int(koniec2)
    
    
    pierwszy = []
    drugi = []
    a1 = poczatek1
    while (a1 <= koniec1):
        pierwszy.append(a1)
        a1 = a1 + 1
    c = 0
    h = 1
    if(poczatek1 == koniec1):
        c = poczatek2
        while(c <= koniec2):
            drugi.append(c)
            c = c + 1
    else:
        while(c < 999):
            drugi.append(h)
            h = h + 1
            c = c + 1
    #wpisywanie tego do tablicy
    end = []
    c = 0
    h = len(pierwszy)
    while(c < h):
        if(h == 1):
            b = poczatek2
            c1 = 0
            while(b <= koniec2):
                if(b <9):
                    if(c < 9 and poczatek1 < 9):
                        end.append('0' + str(pierwszy[c]) + '-' + '00' + str(drugi[c1]))
                    else:
                        end.append(str(pierwszy[c]) + '-' + '00' + str(drugi[c1]))
                elif(b>=9 and b<99):
                    if(c < 9 and poczatek1 < 9):
                        end.append('0' + str(pierwszy[c]) + '-' + '0' + str(drugi[c1]))
                    else:
                        end.append(str(pierwszy[c]) + '-' + '0' + str(drugi[c1]))
                else:
                    if(c < 9 and poczatek1 < 9):
                        end.append('0' + str(pierwszy[c]) + '-' + str(drugi[c1]))
                    else:
                        end.append(str(pierwszy[c]) + '-' + str(drugi[c1]))
                b = b + 1
                c1 += 1
            return end
        if(c == 0):
            b = poczatek2
            while(b < 999):
                if(b <9):
                    if(c < 9 and poczatek1 < 9):
                        end.append('0' + str(pierwszy[c]) + '-' + '00' + str(drugi[b]))
                    else:
                        end.append(str(pierwszy[c]) + '-' + '00' + str(drugi[b]))
                elif(b>=9 and b<99):
                    if(c < 9 and poczatek1 < 9):
                        end.append('0' + str(pierwszy[c]) + '-' + '0' + str(drugi[b]))
                    else:
                        end.append(str(pierwszy[c]) + '-' + '0' + str(drugi[b]))
                else:
                    if(c < 9 and poczatek1 < 9):
                        end.append('0' + str(pierwszy[c]) + '-' + str(drugi[b]))
                    else:
                        end.append(str(pierwszy[c]) + '-' + str(drugi[b]))
                b = b + 1
        elif(c+1 == h):
            b = 0
            while(b < koniec2):
                if(b <9):
                    if(c < 9 and poczatek1 < 9):
                        end.append('0' + str(pierwszy[c]) + '-' + '00' + str(drugi[b]))
                    else:
                        end.append(str(pierwszy[c]) + '-' + '00' + str(drugi[b]))
                elif(b>=9 and b<99):
                    if(c < 9 and poczatek1 < 9):
                        end.append('0' + str(pierwszy[c]) + '-' + '0' + str(drugi[b]))
                    else:
                        end.append(str(pierwszy[c]) + '-' + '0' + str(drugi[b]))
                else:
                    if(c < 9 and poczatek1 < 9):
                        end.append('0' + str(pierwszy[c]) + '-' + str(drugi[b]))
                    else:
                        end.append(str(pierwszy[c]) + '-' + str(drugi[b]))
                b = b + 1
        else:
            b = 0
            while(b < 999):
                if(b <9):
                    if(c < 9 and poczatek1 < 9):
                        end.append('0' + str(pierwszy[c]) + '-' + '00' + str(drugi[b]))
                    else:
                        end.append(str(pierwszy[c]) + '-' + '00' + str(drugi[b]))
                elif(b>=9 and b<99):
                    if(c < 9 and poczatek1 < 9):
                        end.append('0' + str(pierwszy[c]) + '-' + '0' + str(drugi[b]))
                    else:
                        end.append(str(pierwszy[c]) + '-' + '0' + str(drugi[b]))
                else:
                    if(c < 9 and poczatek1 < 9):
                        end.append('0' + str(pierwszy[c]) + '-' + str(drugi[b]))
                    else:
                        end.append(str(pierwszy[c]) + '-' + str(drugi[b]))
                b = b + 1
        c = c + 1
    return end

if(__name__ == "__main__"):
    min = input("Podaj kod pocztowy mniejsza wartość: XX-XXX ")
    max = input("Podaj kod pocztowy większa wartość: XX-XXX ")
    print(kody_pocztowe(min,max))

