try:
    import mysql.connector
    import requests
    import math
    import random
    from datetime import timedelta, date
except:
    print("\nNecessary libraries not available.")

print("\n__________________________________________")
print('\033[1m' + "Welcome to Covid19 Management System\n"
                  " Terms of Service & Privacy-\n"
                  "1.Device Location- This Program requires access to your Rough geographical location.\n"
                  "2.Data Sharing- This Program access to the personal data given by you for Survey Purposes.\n"
                  "NOTE: Any of the Personal Data Confirmed by you will not be disclosed to the Public Domain.\n"
                  "Please Indicate your Acceptance to Terms of Service & Privacy Below:")
print("__________________________________________")

str1 = ("\nWith Covid-19 Management System you can protect yourself,\n"
        "your family and friends, and help our country in the effort to Fight COVID-19.\n"
        "Thank You!" + '\033[0m')

while True:
    Agree = input("\nDo you Agree To our Terms & Conditions[(yes) for yes/(no) for no)]:")
    if Agree == "yes":
        print('Welcome!\n', str1)
        break
    elif Agree == "no":
        print('\nYou Cannot Continue to Access Covid19 Management System without Accepting our Terms & Conditions.')

    else:
        print('\nWrong Input, Please Try Again.')
    continue

mydb = mysql.connector.connect(host='127.0.0.1', user="root", passwd="qwertyuiop")

if mydb.is_connected() == True:
    print("\nSuccessfully Connected to My SQL Database.")

if mydb.is_connected() == False:
    print("\nError Connecting to My SQL Database.")

mycursor = mydb.cursor()

mycursor.execute('create database if not exists Covid19_Management_System')

mycursor.execute("use Covid19_Management_System")

mycursor.execute("create table if not exists staff(ID varchar(25) not null, name varchar(25) not null,"
                 " age varchar(25) not null, gender varchar(25) not null, salary varchar(25) not null, "
                 "date date not null, location varchar(25) not null)")

mycursor.execute("create table if not exists patients(ID varchar(25) not null, name varchar(25) not null,"
                 " age varchar(25) not null, gender varchar(25) not null, date date not null,"
                 " location varchar(25) not null)")

mycursor.execute("create table if not exists login(admin varchar(25) not null,password varchar(25) not null)")

j = 0
mycursor.execute("select* from login")
for i in mycursor:
    j = 1
if j == 0:
    mycursor.execute("insert into login values('Admin','abc')")
    mydb.commit()

loop1 = 'y'
while loop1 == 'y' or loop1 == 'Y':
    try:
        print("\n_______________")
        print("1.Admin Access")
        print("2.Patient-Self Assessment")
        print("3.Covid-19 Data")
        print("4.Vaccine Finder")
        print("5.Exit Application")
        print("_______________")
        ch = int(input("\nSelect Any of the Given Options- [(1)for Admin Access/(2)for Patient Self-Assessment/"
                       "(3)for Covid-19 Data/(4)for Vaccine Finder/(5)Exit Application:"))

        if ch == 1:
            pas = (input("\nEnter Password For Admin Access:"))
            mycursor.execute("select* from login")
            for i in mycursor:
                username, password = i

            if pas == password:  # password is abc
                print("\nYou Have Successfully entered Admin Access.")
                loop2 = 'y'
                while loop2 == 'y' or loop2 == 'Y':
                    try:
                        print("\n_______________")
                        print("1.Add Patients")
                        print("2.Add Staff")
                        print("3.Display Patient's Record")
                        print("4.Display Staff's Record")
                        print("5.Remove Patients")
                        print("6.Remove Staff")
                        print("7.Change Password")
                        print("8.Logout")
                        print("_______________")

                        val = int(input("\nSelect Any of the Given Options- [(1) for Adding Patients/"
                                        "(2) for Adding Staff/(3) for Displaying Patient's Record/"
                                        "(4)for Display Staff's Record/(5)Remove Patients/(6)Remove Staff/"
                                        "(7)Change Password/(8)Logout:"))

                        if val == 1:
                            loop3 = 'y'
                            while loop3 == 'y' or loop3 == "Y":
                                name = input("\nEnter Patient's Name:")

                                try:
                                    aage = input("\nEnter Patient's Age:")
                                    if 0 < int(aage) < 150:
                                        age = str(aage)
                                    else:
                                        age = "Unknown"
                                except:
                                    age = "Unknown"

                                date = date.today()
                                EndDate = date.today() + timedelta(days=14)

                                sgender = (input("\nEnter Patient's Gender[(m) for male/(f) for female)]:"))
                                if sgender == "m" or sgender == "M":
                                    gender = "Male"
                                elif sgender == "f" or sgender == "F":
                                    gender = "Female"
                                else:
                                    gender = "unknown"

                                MyID1 = random.randint(0, 1366500000)
                                print("\nThe ID allotted to you by National Covid Registry is:", MyID1,
                                      "\nPlease Remember This ID for future access.")

                                number = str(input("\nPlease Enter Your Number without any WhiteSpaces:"))
                                location = "-"
                                digits = "0123456789"
                                OTP = ""
                                for i in range(6):
                                    OTP += digits[math.floor(random.random() * 10)]
                                print(OTP)
                                url1 = "https://www.fast2sms.com/dev/bulkV2"

                                querystring = {
                                    "authorization": "GamkM7uA9zjydWSie8pQo3hXbr2Uws4gNPZvtV0TR1F6qBCflOuwdEaAOqF8M41tovTbBzUIPfLp6Hke",
                                    "variables_values": OTP,
                                    "route": "otp",
                                    "numbers": number}

                                headers = {
                                    'cache-control': "no-cache"
                                }

                                response1 = requests.request("GET", url1, headers=headers, params=querystring)


                                while True:
                                    OTP2 = str(input(
                                        "\nEnter your OTP if received or Press Enter to skip the authentication:"))

                                    if OTP == OTP2:
                                        response2 = requests.get(
                                            "http://apilayer.net/api/validate?access_key=764d43592d30e481f0d3e23ae94fc798&number=" + number + "&country_code=IN&format=0")
                                        SET2 = response2.json()
                                        location += SET2["location"]
                                        print("Your Location is ", location)
                                        break
                                    elif OTP2 == "":
                                        print("\nPhone number Authentication skipped.")
                                        break
                                    else:
                                        print("\nGiven Otp is invalid please try again.")

                                mycursor.execute("insert into patients values ('" + str(
                                    MyID1) + "','" + name + "','" + age + "','" + gender + "','" + str(
                                    date) + "','" + location + "')")
                                mydb.commit()

                                mycursor.execute("select * from patients")
                                for i in mycursor:
                                    t_id1, name1, age1, gender1, date1, location1 = i

                                print(f"\nPatient with ID {t_id1} is successfully saved.")

                                print(f"\nThis Patient with ID {t_id1} will be quarantine up to 14 days from",
                                      date.today(),
                                      "to", EndDate)

                                mycursor.execute("select count(*) from patients")
                                data = mycursor.fetchall()
                                count = mycursor.rowcount
                                for m in data:
                                    print(f"\nTotal Number of Patient Registries are", m)

                                loop3 = input("\nDo you Want to Enter more Data On More Patients?"
                                              "[(y) for yes/(n) for no)]:")
                            loop2 = input("\nDo you Want to Stay or Logout?[(y) for Stay/(n) for Logout)]:")

                        elif val == 2:
                            loop3 = 'y'
                            while loop3 == 'y' or loop3 == 'Y':
                                name = input("\nEnter Staff's Name:")

                                try:
                                    aage = input("\nEnter Staff's Age:")
                                    if 0 < int(aage) < 150:
                                        age = str(aage)
                                    else:
                                        age = "Unknown"
                                except:
                                    age = "Unknown"

                                date = date.today()

                                sgender = (input("\nEnter Staff's Gender[(m) for male/(f) for female)]:"))
                                if sgender == "m" or sgender == "M":
                                    gender = "Male"
                                elif sgender == "f" or sgender == "F":
                                    gender = "Female"
                                else:
                                    gender = "Unknown"

                                try:
                                    ssalary = input("\nEnter Staff's Salary in Rupees:")
                                    if 0 < int(ssalary) < 999999999999999999999999:
                                        salary = str(ssalary)
                                    else:
                                        salary = "Unknown"
                                except:
                                    salary = "Unknown"

                                MyID2 = random.randint(0, 1366500000)
                                print("\nThe ID allotted to you by National Covid Registry is:", MyID2,
                                      "\nPlease Remember This ID for future access.")

                                number = str(input("\nPlease Enter Your Number without any WhiteSpaces:"))
                                location = "-"
                                digits = "0123456789"
                                OTP = ""
                                for i in range(6):
                                    OTP += digits[math.floor(random.random() * 10)]
                                print(OTP)

                                url1 = "https://www.fast2sms.com/dev/bulkV2"

                                querystring = {
                                    "authorization": "GamkM7uA9zjydWSie8pQo3hXbr2Uws4gNPZvtV0TR1F6qBCflOuwdEaAOqF8M41tovTbBzUIPfLp6Hke",
                                    "variables_values": OTP,
                                    "route": "otp",
                                    "numbers": number}

                                headers = {
                                    'cache-control': "no-cache"
                                }

                                response1 = requests.request("GET", url1, headers=headers, params=querystring)

                                while True:
                                    OTP2 = str(input(
                                        "\nEnter your OTP if received or Press Enter to skip the authentication:"))

                                    if OTP == OTP2:

                                        response2 = requests.get(
                                            "http://apilayer.net/api/validate?access_key=764d43592d30e481f0d3e23ae94fc798&number=" + number + "&country_code=IN&format=0")
                                        SET2 = response2.json()
                                        location += SET2["location"]
                                        print("Your Location is ", location)
                                        break
                                    elif OTP2 == "":
                                        print("\nPhone number Authentication skipped.")
                                        break
                                    else:
                                        print("\nGiven Otp is invalid please try again.")

                                mycursor.execute("insert into staff values ('" + str(
                                    MyID2) + "','" + name + "','" + age + "','" + gender + "','" + salary + "','" + str(
                                    date) + "','" + location + "')")
                                mydb.commit()

                                mycursor.execute("select* from staff")
                                t = 0
                                for i in mycursor:
                                    t += 1
                                    t_id4, name4, age4, gender4, salary4, date4, location4 = i

                                print(f"\nData Staff with ID {t_id4} is successfully saved.")

                                print(f"\nThis Staff with ID {t_id4} will be hired to work from", date.today())

                                mycursor.execute("select count(*) from staff")
                                data = mycursor.fetchall()
                                count = mycursor.rowcount
                                for m in data:
                                    print(f"\nTotal Number of Staff Registries are", m)

                                loop3 = input("\nDo you Want To Enter More Staff Data?[(y) for yes/(n) for no)]:")
                            loop2 = input("\nDo you Want to Stay or Logout?[(y) for Stay/(n) for Logout)]:")

                        elif val == 3:
                            idd = input("\nEnter Patient's ID:")
                            t_id2, name2, age2, gender2, date2, location2 = ['', '', '', '', '', '']
                            mycursor.execute("select * from patients where ID= '" + idd + "'")
                            for i in mycursor:
                                t_id2, name2, age2, gender2, date2, location2 = i
                            print("\n| ID | NAME | AGE | GENDER | DATE OF CONFIRMATION OF COVID-19 | LOCATION")
                            print(f"\n| {t_id2} | {name2} | {age2} | {gender2} | {date2} | {location2}")

                            mycursor.execute("select count(*) from patients")
                            data = mycursor.fetchall()
                            count = mycursor.rowcount
                            for m in data:
                                print(f"\nTotal Number of Patient Registries are", m)

                        elif val == 4:
                            idd = input("\nEnter Staff's ID:")
                            t_id3, name3, age3, gender3, salary3, date3, location3 = ['', '', '', '', '', '', '']
                            mydb.commit()
                            mycursor.execute("Select * from staff where ID='" + idd + "'")
                            for i in mycursor:
                                t_id3, name3, age3, gender3, salary3, date3, location3 = i
                            print("\n| ID | NAME | AGE | GENDER | SALARY | DATE OF JOINING | LOCATION")
                            print(f"\n| {t_id3} | {name3} | {age3} | {gender3} | {salary3} | {date3} | {location3}")

                            mycursor.execute("select count(*) from staff")
                            data = mycursor.fetchall()
                            count = mycursor.rowcount
                            for m in data:
                                print(f"\nTotal Number of Staff Registries are", m)

                        elif val == 5:
                            loop3 = 'y'
                            while loop3 == "y" or loop3 == "Y":
                                idd = input("\nEnter Patient's ID:")
                                mycursor.execute("delete from patients where ID='" + idd + "'")
                                mydb.commit()
                                print("\nPatient has been removed Successfully.")

                                mycursor.execute("select count(*) from patients")
                                data = mycursor.fetchall()
                                count = mycursor.rowcount
                                for m in data:
                                    print(f"\nTotal Number of Patient Registries are", m)

                                    loop3 = input("\nDo you Want to Remove More Patients?[(y) for yes/(n) for no)]:")

                        elif val == 6:
                            loop3 = 'y'
                            while loop3 == "y" or loop3 == "Y":
                                idd = input("\nEnter Staff's ID:")
                                mycursor.execute("delete from Staff where ID='" + idd + "'")
                                mydb.commit()
                                print("\nStaff has been removed Successfully.")

                                mycursor.execute("select count(*) from staff")
                                data = mycursor.fetchall()
                                count = mycursor.rowcount
                                for m in data:
                                    print(f"\nTotal Number of Staff Registries are", m)

                                    loop3 = input("\nDo you Want to Remove More Staff?[(y) for yes/(n) for no)]:")

                        elif val == 7:
                            pas = input("\nEnter Old Password:")
                            mycursor.execute("select* from login")
                            for i in mycursor:
                                username, password = i
                            if pas == password:
                                npas = input("\nEnter New Password:")
                                mycursor.execute("Update login set password='" + npas + "'")
                                mydb.commit()
                                print("\nYou Have Successfully Updated Your Password.")
                            else:
                                print("\nWrong Password...")

                        elif val == 8:
                            print("\nYou have Successfully Logged out.")
                            break
                    except:
                        print("Wrong Input, Try Again!")
            else:
                print("\nWrong Password...")

        elif ch == 2:
            try:
                print("\n__________________________________________")
                print("Thank you for Enrolling In our Patient-Self Assessment Program.\n"
                      "Please note that your inputs will supplement the efforts being taken "
                      "to contain corona pandemic and\n"
                      " assess the  the symptoms of patients.Please help Us Prevent the spread of COVID-19.")
                print("__________________________________________")

                cough = input("\nAre you Feeling Cough[(y) for yes/(n) for no)]?:").lower()
                dry_cough = "n"
                if cough == 'y' or cough == 'Y':
                    dry_cough = input("\nAre you Feeling Dry Cough[(y) for yes/(n) for no)]?").lower()
                sore_throat = input("\nAre you feeling sore_throat?[(y) for yes/(n) for no)]:").lower()
                runny_nose = input("\nAre you Having Runny Nose?[(y) for yes/(n) for no)]:").lower()
                body_ache = input("\nAre you Having Body ache?[(y) for yes/(n) for no)]:").lower()
                weakness = input("\nAre you feeling Weakness?[(y) for yes/(n) for no)]:").lower()
                chest_congestion = input("\nAre you  Having Chest_Congestion?[(y) for yes/(n) for no)]:").lower()
                breath = input("\nAre you Having Difficulty in Breathing?[(y) for yes/(n) for no)]:").lower()
                temp = (
                    input("\nIs Your Body Temperature Above 100 degrees fahrenheit?[(y) for yes/(n) for no)]:")).lower()

                if dry_cough == 'y' and sore_throat == 'y' and body_ache == 'y' and weakness == 'y' and \
                        temp == 'y' and breath == 'y':
                    print("\n__________________________________________")
                    print('According to our Estimates, Your Chances of infection are high,\n'
                          'we recommend that you stay at home to avoid any possible chances '
                          'of transmission of COVID-19 and\n'
                          'Get COVID-19 Confirmatory test from nearest govt hospital as soon as possible.')
                    print("__________________________________________")
                    name = input("\nEnter your Name:")

                    try:
                        aage = input("\nEnter Patient's Age:")
                        if 0 < int(aage) < 150:
                            age = str(aage)
                        else:
                            age = "Unknown"
                    except:
                        age = "Unknown"

                    date = date.today()
                    EndDate = date.today() + timedelta(days=14)

                    sgender = (input("\nEnter Patient's Gender[(m) for male/(f) for female)]:"))
                    if sgender == "m" or sgender == "M":
                        gender = "Male"
                    elif sgender == "f" or sgender == "F":
                        gender = "Female"
                    else:
                        gender = "Unknown"

                    MyID3 = random.randint(0, 1366500000)
                    print("\nThe ID allotted to you by National Covid Registry is:", MyID3,
                          "\nPlease Remember This ID for future access.")

                    number = str(input("\nPlease Enter Your Number without any WhiteSpaces:"))
                    location = "-"
                    digits = "0123456789"
                    OTP = ""
                    for i in range(6):
                        OTP += digits[math.floor(random.random() * 10)]
                    print(OTP)
                    url1 = "https://www.fast2sms.com/dev/bulkV2"

                    querystring = {
                        "authorization": "GamkM7uA9zjydWSie8pQo3hXbr2Uws4gNPZvtV0TR1F6qBCflOuwdEaAOqF8M41tovTbBzUIPfLp6Hke",
                        "variables_values": OTP,
                        "route": "otp",
                        "numbers": number}

                    headers = {
                        'cache-control': "no-cache"
                    }

                    response1 = requests.request("GET", url1, headers=headers, params=querystring)

                    while True:
                        OTP2 = str(input("\nEnter your OTP if received or Press Enter to skip the authentication:"))

                        if OTP == OTP2:
                            response2 = requests.get(
                                "http://apilayer.net/api/validate?access_key=764d43592d30e481f0d3e23ae94fc798&number=" + number + "&country_code=IN&format=0")
                            SET2 = response2.json()
                            location += SET2["location"]
                            print("Your Location is ", location)
                            break
                        elif OTP2 == "":
                            print("\nPhone number Authentication skipped.")
                            break
                        else:
                            print("\nGiven Otp is invalid please try again.")

                    mycursor.execute("insert into patients values ('" + str(
                        MyID3) + "','" + name + "','" + age + "','" + gender + "','" + str(
                        date) + "', '" + location + "')")
                    mydb.commit()

                    mycursor.execute("select * from patients")
                    for i in mycursor:
                        t_id5, name5, age5, gender5, date5, location5 = i

                    print(f"\nData of Patient with ID {t_id5} is successfully saved.")

                    print(f"\nThis Patient with ID {t_id5} will be quarantine up to 14 days from", date.today(), "to",
                          EndDate)

                    mycursor.execute("select count(*) from patients")
                    data = mycursor.fetchall()
                    count = mycursor.rowcount
                    for m in data:
                        print(f"\nTotal Number of Patient Registries are", m)


                elif dry_cough == 'y' and sore_throat == 'n' and body_ache == 'n' and weakness == 'n' \
                        and temp == 'n' and breath == 'y':
                    print("\n__________________________________________")
                    print("According to Our Estimates, You are Suffering From Excessive Air Pollution\n"
                          " we recommend that you stay at home to avoid any chances of exposure to or"
                          "possible transmission of COVID-19\n"
                          " and monitor your health condition over the period of two weeks.")
                    print("__________________________________________")

                elif cough == 'y' and chest_congestion == 'y' and runny_nose == 'y' and sore_throat == "n" \
                        and body_ache == 'n' and weakness == 'n' and breath == 'n':
                    print("\n__________________________________________")
                    print("According to Our Estimates, You are Suffering Form Common Cold\n"
                          " we recommend that you stay at home to avoid any chances of exposure to or "
                          "possible transmission of COVID-19\n"
                          " and monitor your health condition over the period of two weeks.")
                    print("__________________________________________")

                elif cough == 'y' and dry_cough == 'n' and chest_congestion == 'y' and runny_nose == 'y' \
                        and sore_throat == "n" and temp == 'y' and breath == 'n':
                    print("\n__________________________________________")
                    print("According to Our Estimates, You are Suffering From Flu\n"
                          " we recommend that you stay at home to avoid any chances of exposure to or "
                          "possible transmission of COVID-19\n"
                          " and monitor your health condition over the period of two weeks.")
                    print("__________________________________________")

                elif cough != 'y' and dry_cough != 'y' and chest_congestion != 'y' and runny_nose != 'y' \
                        and sore_throat != "y" and body_ache != 'y' and temp != 'y' and breath != 'y':
                    print("__________________________________________")
                    print("\nAccording to Our Estimates, Your chances of infection are low\n"
                          " we recommend that you stay at home to avoid any chances of exposure to or "
                          "possible transmission of COVID-19\n"
                          " and monitor your health condition over the period of two weeks.")
                    print("__________________________________________")
                else:
                    print("\n__________________________________________")
                    print("According to Our Estimates, Your Chances of infection are moderate,\n"
                          " we recommend that you stay at home to avoid any chances of exposure to COVID-19 and\n"
                          " retake the self assessment tests if you develop symptoms or come in contact "
                          "with COVID-19 confirmed patient.")
                    print("__________________________________________")
            except:
                print("Wrong Input, Try Again!")

        elif ch == 3:
            loop4 = 'y'
            while loop4 == 'y' or loop4 == 'Y':
                try:
                    print("\n_______________")
                    print("1.National Covid-19 Data")
                    print("2.StateWise Covid-19 Data")
                    print("3.Logout")
                    print("_______________")

                    url3 = "https://covid-19-india2.p.rapidapi.com/details.php"

                    headers = {
                        'x-rapidapi-host': "covid-19-india2.p.rapidapi.com",
                        'x-rapidapi-key': "42af268ae1msh69c0c3fd1bcab97p16eff4jsn025141ebff31"
                    }

                    response3 = requests.request("GET", url3, headers=headers)
                    SET3 = response3.json()

                    ton = int(input("\nSelect Any of the Given Options- [(1)for National Covid-19 Data/"
                                    "(2)for StateWise Covid-19 Data/(3)Logout]:"))

                    if ton == 1:

                        ind = SET3["Total"]
                        print("\n_______________________")
                        print('\033[1m' + "Data Regarding current Covid-19 Cases Nationally-" + '\033[0m')
                        print("Active Covid-19 Cases", ind["confirm"])
                        print("Total Covid-19 Deaths", ind["death"])
                        print("Total Recovered Covid-19 Cases", ind["cured"])
                        print("Data Last Updated", SET3["lastupdated"])
                        print("__________END__________")

                    elif ton == 2:

                        loop5 = "y"
                        while loop5 == 'y' or loop5 == 'Y':
                            try:
                                state_name = str(input("Enter the  Name of the State (Eg- Delhi or Gujarat):"))
                                state = SET3[state_name]
                                print("\n_______________________")
                                print('\033[1m' + "Data Regarding current Covid-19 Cases of State-",
                                      state_name + '\033[0m')
                                print("Active Covid-19 Cases", state["confirm"])
                                print("Total Covid-19 Deaths", state["death"])
                                print("Total Recovered Covid-19 Cases", state["cured"])
                                print("Data Last Updated", SET3["lastupdated"])
                                print("__________END__________")
                                loop5 = input(
                                    "\nDo you Want to Lookup for Statewise Covid-19 Cases Again?[(y) for yes/(n) for no)]:")
                            except:
                                print("The is no such state named", state_name)
                                loop5 = input(
                                    "\nDo you Want to Lookup for More StateWise Covid-19 Cases?[(y) for yes/(n) for no)]:")


                    elif ton == 3:
                        print("\nYou have Successfully Logged out.")
                        break
                    else:
                        print("\nWrong Input, Please Try Again.")
                except:
                    print("\nWrong Input, Please Try Again.")

        elif ch == 4:
            loop6 = 'y'
            while loop6 == 'y' or loop5 == 'Y':
                try:
                    datex = str(input("\nEnter the date you would like to vaccinate of the format XX-XX-20XX:"))
                    pin = str(input("\nEnter The pin of your locality to Lookup nearby Vaccination Centres:"))

                    header = {
                        'accept': 'application/json',
                        'Accept-Language': 'US_IN',
                    }

                    param = {
                        ('pincode', pin),
                        ('date', datex),
                    }
                    # Data Is Generally Available only for days of present or the close coming days only.
                    response4 = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin',
                                             headers=header,
                                             params=param)
                    sett = response4.json()
                    data = sett["sessions"]
                    counter = 0
                    for each in data:
                        if (each["available_capacity"] > 0) & (each["min_age_limit"] == 18):
                            counter += 1
                            print("\n__________________________________________")
                            print("The Address of the Hospital With Vaccines Available is", each["address"])
                            print("The Time Slots Available For Vaccination is", each["slots"])
                            print("The Vaccine Available is", each["vaccine"])
                            print("The Fee for the Vaccine is", each["fee"])
                            print("The Available Capacity for the Vaccine is", each["available_capacity"])
                            print("__________________________________________")
                    if counter == 0:
                        print("\nNo Available Slots for the given Date in the Area of the given Pin code.")

                    loop6 = input(
                        "\nDo you Want to Lookup Available Vaccination Slots Again?[(y) for yes/(n) for no)]:")

                except:
                    print("\nThe Given Data in Incorrect, Please Try Again.")

        elif ch == 5:
            print('\033[1m'"\nYou have Successfully Exited Covid-19 Managment System.")
            print("\nThank you." + '"\033[0m')
            break
    except:
        print("Wrong Input, Try Again!")

mydb.close()
