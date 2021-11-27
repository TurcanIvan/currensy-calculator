#types
#operations
# i/o

###################

1    #int
1.2  #float
# in > USD >>> APP >>> EUR  > out
money_usd = input("Enter your money USD : ")
#type casting : int ( ... , foat ( ... ), Str( ... ),...
money_usd = float(money_usd)

usd_2_eur = 0.9 #1 USD ->0.9 EUR


money_eur = money_usd * usd_2_eur

print("yor money in EUR : ",money_eur)

####################
# money_usd <<< input() <<< '100'
# money_usd <<< float( '100' ) <<< 100
# money_usd * usd_2_eur