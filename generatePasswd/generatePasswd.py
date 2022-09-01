import sys

CommonPasswd = [
    "123456",
    "1",
    "1234",
    "123",
    "12346",
    "123456789",
    "root",
    "admin",
    "1qaz@WSX",
    "!QAZ2wsx",
    "Passw0rd@_",
    "Passw0rd@",
    "Passw0rd",
    "111111",
    "654321",
    "!@#123qwe@!#",
    "Password@_",
    "jydadmin",
    "adminadmin123111111",
    "Aa123456",
    "admin123"

]
DictRules = [
    "{}2015",
    "{}2016",
    "{}2017",
    "{}2018",
    "{}2019",
    "{}2020",
    "{}2021",
    "{}2022",
    "{}@2015",
    "{}@2016",
    "{}@2017",
    "{}@2018",
    "{}@2019",
    "{}@2020",
    "{}@2021",
    "{}@2022",
    "{}@2015!",
    "{}@2016!",
    "{}@2017!",
    "{}@2018!",
    "{}@2019!",
    "{}@2020!",
    "{}@2021!",
    "{}@2022!",
    "{}2015!",
    "{}2016!",
    "{}2017!",
    "{}2018!",
    "{}2019!",
    "{}2020!",
    "{}2021!",
    "{}2022!",
    "{}1234",
    "{}123",
    "{}12345",
    "{}123456",
    "{}12346",
    "{}1234!",
    "{}123!",
    "{}12345!",
    "{}12346!",
    "{}@1234",
    "{}@123",
    "{}@12345",
    "{}@12346",
    "{}@Passw0rd@_",
    "Passw0rd@{}",
    "{}123!@#",
    "{}@123!@#",
    "{}admin123"

]
passOutputDict = []
def generatePasswd(target):
    rule = ["up_1","up_-1","all_upper","all_low"]
    if len(target)!=0:
        for r in rule:
            tmpTarget = target
            if "up_1" == r:
                tmpTarget = list(tmpTarget)
                tmpTarget[0] = tmpTarget[0].upper()
                tmpTarget = "".join(tmpTarget)
                for pwd in DictRules:
                    password = pwd.format(tmpTarget)
                    passOutputDict.append(password)
            if "up_-1" ==r:
                tmpTarget = list(tmpTarget)
                tmpTarget[-1] == tmpTarget[-1].upper()
                tmpTarget = "".join(tmpTarget)
                for pwd in DictRules:
                    password = pwd.format(tmpTarget)
                    passOutputDict.append(password)
            if "all_upper" == r:
                tmpTarget = tmpTarget.upper()
                for pwd in DictRules:
                    password = pwd.format(tmpTarget)
                    passOutputDict.append(password)
            if "all_low" ==r:
                tmpTarget = tmpTarget.lower()
                for pwd in DictRules:
                    password = pwd.format(tmpTarget)
                    passOutputDict.append(password)
    for pwd in CommonPasswd:
        passOutputDict.append(pwd)

    for pwd in DictRules:
        passOutputDict.append(pwd.format(target))

    return list(set(passOutputDict))

for passwd in generatePasswd(sys.argv[1]):
    print(passwd)