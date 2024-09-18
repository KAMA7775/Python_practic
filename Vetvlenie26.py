pervoe_chislo = int(input("pevoe chislo"))
vtoroe_chislo = int(input("vtoroe chislo"))
tretye_chislo = int(input("tretye chislo"))
chrvertoe_chislo = int(input("chrvertoe chislo"))
pyatoe_chislo = int(input("pyatoe chislo"))
if  pervoe_chislo >= vtoroe_chislo and pervoe_chislo >= tretye_chislo and pervoe_chislo >= chrvertoe_chislo and pervoe_chislo >= pyatoe_chislo:
    max_chislo = pervoe_chislo
elif vtoroe_chislo >= pervoe_chislo and vtoroe_chislo >= tretye_chislo and vtoroe_chislo >= chrvertoe_chislo and vtoroe_chislo >= pyatoe_chislo:
    max_chislo = vtoroe_chislo
elif tretye_chislo >= pervoe_chislo and tretye_chislo >= vtoroe_chislo and tretye_chislo >= chrvertoe_chislo and tretye_chislo >= pyatoe_chislo:
    max_chislo = tretye_chislo
elif chrvertoe_chislo >= pervoe_chislo and chrvertoe_chislo >= vtoroe_chislo and chrvertoe_chislo >= tretye_chislo and chrvertoe_chislo >= pyatoe_chislo:
    max_chislo = chrvertoe_chislo
else:
    max_chislo = pyatoe_chislo

print("Naibolshee chislo:", max_chislo)
