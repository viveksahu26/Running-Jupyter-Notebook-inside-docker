#! /usr/bin/python3

print("content-type: text/html")
print()


print('''<style>
pre{
color: black;
font-weight: bold;
font-size: 30px;
}
</style>''')


import cgi
import subprocess as sb

fs = cgi.FieldStorage()

plate_no = fs.getvalue("plate_no")


if plate_no == "MHI2 DE1433":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : Vimal Daga 
    License No : 234554667889
    Make / Model : YASH MOTORS HYUNDAI / VERNA
    Registration Date : 12/1/2016
    Registering Authority : JAIPUR , INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 15/10/2016
    Fitness Upto : 14/10/2040
    </pre>''')
    print("</body>")

elif plate_no == "MH:01.CT.5470":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : MS DHONI
    License No : 098363357292
    Make / Model : BUGATI / VERRON
    Registration Date : 7/7/2014
    Registering Authority : RANCHI, INDIA
    Vehicle Class : MCWG
    Fuel Type : PETROL
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2050
    Fitness Upto : 4/8/2050
    </pre>''')
    print("</body>")

elif plate_no == "HR26 CJ 1818":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : VIRAT KOHLI
    License No : 098363357292
    Make / Model : ROLLS ROYCE
    Registration Date : 11/12/2016
    Registering Authority : MUMBAI, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2042
    Fitness Upto : 4/8/2050
    </pre>''')
    print("</body>")

elif plate_no == "TS09FJ0005":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : YUVRAJ SINGH
    License No : 098363357292
    Make / Model : MERCEDES / BENZ
    Registration Date : 12/12/2014
    Registering Authority : PUNJAB, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2032
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

elif plate_no == "P4TVN":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : SURESH RAINA
    License No : 098363357292
    Make / Model : JAGUAR / E24
    Registration Date : 1/12/2028
    Registering Authority : MUMBAI, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVKDJ452KKB4538
    Chassis No : HMWOGJSAHWSVWE
    Insurance Upto : 5/13/2024
    Fitness Upto : 4/8/2033
    </pre>''')
    print("</body>")


elif plate_no == "MH 12 HZ 0148":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : AMAN PANWAR
    License No : 735382528936
    Make / Model : MARUTI SUZUKI / ALTO800
    Registration Date : 1/12/2014
    Registering Authority : MANDSAUR, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")