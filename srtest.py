import requests
import csv
import os
import pandas

# Insert SEM_Rush_API_key from SEM Rush
SEM_Rush_API_key = ''

#insert URL for websites to be called
Domain = input ("Enter a URL:")

# API Calls
URL = 'https://api.semrush.com/?type=domain_ranks&export_columns=Db,Dn,Rk,Or,Ot,Oc,Ad,At,Ac,Sv,Sh&domain=' + Domain + '&key=' + SEM_Rush_API_key
URL2 = 'https://api.semrush.com/?type=domain_adwords&display_limit=10&export_columns=Ph,Po,Pp,Pd,Nq,Cp,Vu,Tr,Tc,Co,Nr,Td&domain=' + Domain +'&database=us' + '&key=' + SEM_Rush_API_key
URL3 = 'https://api.semrush.com/?type=domain_organic&display_filter=%2B%7CPh%7CCo%7Cseo&display_limit=10&export_columns=Ph,Po,Pp,Pd,Nq,Cp,Ur,Tr,Tc,Co,Nr,Td&domain=' + Domain + '&key=' + SEM_Rush_API_key + '&database=us'
URL4 = 'https://api.semrush.com/?type=url_organic&display_limit=10&export_columns=Ph,Po,Nq,Cp,Co,Tr,Tc,Nr,Td&url=' + Domain + '&database=us' + '&key=' + SEM_Rush_API_key

# Requests
r = requests.get(URL)
r2 = requests.get(URL2)
r3 = requests.get(URL3)
r4 = requests.get(URL4)

# Text Pull
lm = r.text
lm2 = r2.text
lm3 = r3.text
lm4 = r4.text

# Replace for CSV proper Form for ETL
j = lm.replace(';',',')
j2 = lm2.replace(';',',')
j3 = lm3.replace(';',',')
j4 = lm4.replace(';',',')

# Creation of CSVs for each Report
file = open(Domain +'Overview.csv', "w",)
file.write(j)
file.close()
file = open(Domain +'PaidKeywords.csv', "w",)
file.write(j2)
file.close()
file = open(Domain +'DomainOrganicKeywords.csv', "w",)
file.write(j3)
file.close()
file = open(Domain +'URLOrganicKeywords.csv', "w",)
file.write(j4)
file.close()

# Results Check
print(j)
print(j2)
print(j3)
print(j4)
print(URL)
print(URL2)
print(URL3)
print(URL4)
