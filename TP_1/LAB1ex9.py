#Problem9
def electricity_bill(kwh):
    if kwh<0:
        return None
    tier1=min(kwh,50)*480
    tier2=min(max(kwh-50,0),150)*610
    tier3=max(kwh-200,0)*730
    total=(tier1+tier2+tier3+2000)*1.10
    return round(total)
print("Table:")
for kwh in[0,35,50,120,200,350]:
    bill=electricity_bill(kwh)
    bill_usd=bill/4100
    print(str(kwh)+"kwh->"+format(bill,",")+"riel(≈"+str(round(bill_usd,2))+"USD)")

try:
    user_kwh=float(input("\nEnter your montly cpnsumption(kwh):"))
    bill=electricity_bill(kwh)
    if bill is None:
        print("Invalid")
    else:
        print("Your bill:"+format(bill,",")+"riel(≈"+str(round(bill/4100,2))+"USD)")
except ValueError:
    print("Invalid input!Please enter a valid number.")