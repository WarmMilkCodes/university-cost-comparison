purdue_credit_hour_cost = 371
msu_credit_hour_cost = 223

credits_required = 180 #bachelor's degree requirement
msu_cost = 223*12 #cost per semseter / full-time
purdue_cost = 371*12

print("\n$" + str(msu_cost) + " MSU cost per semester")
print("$" + str(purdue_cost) + " PGU cost per semester")

msu_bs = msu_cost*15 #cost for MSU Bachelor Degree (estimate)
purdue_bs = purdue_cost*15

print('\n$' + str(msu_bs) + ' total estimated MSU cost')
print('$' + str(purdue_bs) + ' total estimated PGU cost')

if msu_bs > purdue_bs:
    print("\nMSU Costs More by $" + str(msu_bs%purdue_bs))
else:
    print("\nPurdue Global Costs More by $" + str(purdue_bs%msu_bs))
    print("\n")