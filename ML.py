def reg():
    print('1 - Alaska\n2 - Alabama\n3 - Arkansas\n4 - Arizona\n5 - California\n6 - Colorado\n7 - Connecticut\n8 - District of Columbia\n9 - Delaware\n10 - Florida\n11 - Georgia\n12 - Hawaii\n13 - Iowa\n14 - Idaho\n15 - Illinois\n16 - Indiana\n17 - Kansas\n18 - Kentucky\n19 - Louisiana\n20 - Massachusetts\n21 - Maryland\n22 - Maine\n23 - Michigan\n24 - Minnesota\n25 - Missouri\n26 - Mississippi\n27 - Montana\n28 - North Carolina\n29 - North Dakota\n30 - Nebraska\n31 - New Hampshire\n32 - New Jersey\n33 - New Mexico\n34 - Nevada\n35 - New York\n36 - Ohio\n37 - Oklahoma\n38 - Oregon\n39 - Pennsylvania\n40 - Puerto Rico\n41 - Rhode Island\n42 - South Carolina\n43 - South Dakota\n44 - Tennessee\n45 - Texas\n46 - Utah\n47 - Virginia\n48 - Vermont\n49 - Washington\n50 - Wisconsin\n51 - West Virginia\n52 - Wyoming')
    a=int(input("Rural_urban_continuum_code_2013 of your County: "))
    b=float(input("Unemployment_rate_2007: "))
    c=float(input("Unemployment_rate_2008: "))
    d=float(input("Unemployment_rate_2009: "))
    e=float(input("Unemployment_rate_2010: "))
    f=float(input("Unemployment_rate_2011: "))
    g=float(input("Unemployment_rate_2012: "))
    h=float(input("Unemployment_rate_2013: "))
    i=float(input("Unemployment_rate_2014: "))
    j=float(input("Unemployment_rate_2015: "))
    k=float(input("Unemployment_rate_2016: "))
    l=float(input("Unemployment_rate_2017: "))
    m=float(input("Med_HouseHold_Income_Percent_of_State_Total_2017: "))
    n=float(input("State (Give the number as seen above) : "))
    if(a>10 or a<1):
        print("Incorrect Rural_urban_continuum_code_2013!! Should be between 1-9 ")
    elif(b<0 or b>101):
        print("Incorrect Unemployment_rate_2007. Should be between 0-100")
    elif(c<0 or c>101):
        print("Incorrect Unemployment_rate_2008. Should be between 0-100")
    elif(d<0 or d>101):
        print("Incorrect Unemployment_rate_2009. Should be between 0-100")
    elif(e<0 or e>101):
        print("Incorrect Unemployment_rate_2010. Should be between 0-100")
    elif(f<0 or f>101):
        print("Incorrect Unemployment_rate_2011. Should be between 0-100")
    elif(g<0 or g>101):
        print("Incorrect Unemployment_rate_2012. Should be between 0-100")
    elif(h<0 or h>101):
        print("Incorrect Unemployment_rate_2013. Should be between 0-100")
    elif(i<0 or i>101):
        print("Incorrect Unemployment_rate_2014. Should be between 0-100")
    elif(j<0 or j>101):
        print("Incorrect Unemployment_rate_2015. Should be between 0-100")
    elif(k<0 or k>101):
        print("Incorrect Unemployment_rate_2016. Should be between 0-100")
    elif(l<0 or l>101):
        print("Incorrect Unemployment_rate_2017. Should be between 0-100")
    elif(m<0 or m>101):
        print("Incorrect Med_HouseHold_Income_Percent_of_State_Total_2017. Should be between 0-100")
    elif(n<0 or n>101):
        print("Incorrect State Number. Should be between 0-52")
    else:
        ur=0.143+(0.018*a)+(0.036*b)+(0.044*c)-(0.044*d)-(0.016*e)-(0.036*f)+(0.074*g)+(0.007*h)-(0.039*i)+(0.187*j)-(0.138*k)+(0.799*l)+(0.002*m)+(0.006*n)
        print("Predicted Unemplyment Rate is",ur)
    op=int(input("press 1 if you want to repeat and other buttons to exit: "))
    if(op==1):
        reg()
    else:
        exit
reg()
