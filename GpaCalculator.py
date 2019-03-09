fen_sayi = int(input(" Fənnlərinizin sayını daxil edin: "))  #insert count of subjects
daxil_edilen= 0 
bal_cem = 0  # total sum of grades
while daxil_edilen < fen_sayi:
    bal=float(input(str(daxil_edilen+1) +" . fənn üçün balı daxil edin: "))
    print("Daxil edilen bal:",str(bal))
    daxil_edilen+=1  # counter for subjects
    bal_cem+=bal  # to find sum of grades
    print("-----------")
ortabal=bal_cem/daxil_edilen  #to calculate average grade point
print("Sizin orta balınız : "+str(ortabal))  #out the final result to screen

