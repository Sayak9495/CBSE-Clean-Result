import sqlite3

(lst,item,k,sub,sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8,sub9,sub10,sub11,sub12,sub13,name)=([],[],0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,'')

def subcalc(subcode):
    if subcode=="301" : subname="English Core"
    if subcode=="042" : subname="Physics"
    if subcode=="043" : subname="Chemistry"
    if subcode=="044" : subname="Biology"
    if subcode=="065" : subname="Informatics Practice"
    if subcode=="030" : subname="Economics"
    if subcode=="054" : subname="Business Studies"
    if subcode=="055" : subname="Acountancy"
    if subcode=="041" : subname="Mathematics"
    if subcode=="027" : subname="History"
    if subcode=="028" : subname="Political Science"
    if subcode=="039" : subname="Sociology"
    if subcode=="048" : subname="Physical Education"
    try:
        sub1=float(line[line.find(subcode)+4:line.find(subcode)+7])
        print subname,sub1
        return sub1
    except:
        print "Something Went Wrong - Can't find Sub Marks(Either AB or Fail )"
        sub1=0
        print subname,sub1
        return sub1




fh=raw_input("Enter CBSE result txt : ")
#fh="08153.TXT"
fh1=open(fh)
d=dict()

conn = sqlite3.connect(fh[:5] + '.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS CBSEresult (Roll INTEGER Primary Key,Name TEXT,Percentage_Top5 INTEGER,Physics INTEGER,Chemistry INTEGER,Mathematics INTEGER,IP INTEGER,English INTEGER,Biology INTEGER,Economics INTEGER,Business_Studies INTEGER,Acountancy INTEGER,History INTEGER,Pol_Sci INTEGER,Sociology INTEGER,PHE INTEGER,School TEXT)''')


for line in fh1:
    if line.startswith("SCHOOL"):
        schoolname=line[15:40]
    
    if line.startswith("76"):
        roll=line[0:8]
        print roll
        lst=line.split()
        
                
        for i in lst[1:3]:
            if i == "301" : continue
            name=name+i+' '
        print name
        
        if "301" in line:
            k=k+1
            try:
                sub1=float(subcalc("301"))
                sub=sub+sub1
                item.append(sub1)
            except:
                print "Invalid Value"
        if "042" in line:
            k=k+1
            try:
                sub2=float(subcalc("042"))
                sub=sub+sub2
                item.append(sub2)
            except:
                print "Invalid Value"
        if "043" in line:
            k=k+1
            try:
                sub3=float(subcalc("043"))
                sub=sub+sub3
                item.append(sub3)
            except:
                print "Invalid Value"
        if "044" in line:
            k=k+1
            try:
                sub4=float(subcalc("044"))
                sub=sub+sub4
                item.append(sub4)
            except:
                print "Invalid Value"
        if "065" in line:
            k=k+1
            try:
                sub5=float(subcalc("065"))
                sub=sub+sub5
                item.append(sub5)
            except:
                print "Invalid Value"
        if "030" in line:
            k=k+1
            try:
                sub6=float(subcalc("030"))
                sub=sub+sub6
                item.append(sub6)
            except:
                print "Invalid Value"
        if "054" in line:
            k=k+1
            try:
                sub7=float(subcalc("054"))
                sub=sub+sub7
                item.append(sub7)
            except: 
                print "Invalid Value"
        if "055" in line:
            k=k+1
            try:
                sub8=float(subcalc("055"))
                sub=sub+sub8
                item.append(sub8)
            except:
                print "Invalid Value"
        if "041" in line:
            k=k+1
            try:
                sub9=float(subcalc("041"))
                sub=sub+sub9
                item.append(sub9)
            except:
                print "Invalid Value"
        if "027" in line:
            k=k+1
            try:
                sub10=float(subcalc("027"))
                sub=sub+sub10
                item.append(sub10)
            except:
                print "Invalid Value"
        if "028" in line:
            k=k+1
            try:
                sub11=float(subcalc("028"))
                sub=sub+sub11
                item.append(sub11)
            except:
                print "Invalid Value"
        if "039" in line:
            k=k+1
            try:
                sub12=float(subcalc("039"))
                sub=sub+sub12
                item.append(sub12)
            except:
                print "Invalid Value"
        if "048" in line:
            k=k+1
            try:
                sub13=float(subcalc("048"))
                sub=sub+sub13
                item.append(sub13)
            except:
                print "Invalid Value"
        
        item.sort()
        if k == 6:
            sub=0
            print "Top 5 Subject : "
            for x in item[1:]:
                print x
                sub=sub+x
        if k == 7:
            sub=0
            print "Top 5 Subject : "
            for x in item[2:]:
                print x
                sub=sub+x
        try:
            percentage = sub/5
            print "Percentage",percentage
            print k
        except:
            "K is ZERO"
        print "**************************************************"
        
        try:
            cur.execute(' INSERT INTO CBSEresult (Roll,Name,Percentage_Top5,Physics,chemistry,Mathematics,IP,English,Biology,Economics,Business_Studies,Acountancy,History,Pol_Sci,Sociology,PHE,School) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)' , (roll,name,percentage,sub2,sub3,sub9,sub5,sub1,sub4,sub6,sub7,sub8,sub10,sub11,sub12,sub13,schoolname))
        except:
            print "Already Inseted"
                        
        (item,k,sub,sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8,sub9,sub10,sub11,sub12,sub13,name)=([],0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,'')
        
               
conn.commit()
#print cur.execute("SELECT * FROM CBSEresult")
#print "*********************************************"

#for row in cur.execute("SELECT * FROM CBSEresult"):
#    print row[1],"  ",row[0]


'''
#to export as csv file
with open("CBSEresult.csv", "wb") as write_file:
     cur = conn.cursor()
     for row in cur.execute("SELECT * FROM CBSEresult"):
            #writeRow = " ".join([str(i) for i in row])
            #writeRow = "".join(str(row))
            row=str(row)[1:len(str(row))-1]
            write_file.write(str(row))
            write_file.write("\n")

'''