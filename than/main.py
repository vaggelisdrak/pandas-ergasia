import pandas as pd

def open_file():

    file_name = 'GrCensus2011.xlsx'

    
    # read  an excel file
    df = pd.read_excel(file_name)
    print(df)

    
    #----------------------------------------------------- 1o erotima

    df1 = pd.read_excel(file_name, usecols='C,D') #get column C,D 
    #print(df1)
    
    mylist1 = df1.values.tolist() 
    #print(mylist2)

    plithismos = []
    for i in mylist1[5:]:
        if 'ΔΗΜΟΣ' in i[0]:
            plithismos.append(int(i[1]))

    #print(max(plithismos))

    for j in mylist1:
        if j[1] == max(plithismos):
            print('o megistos plithismos einai: ',j[0],j[1])
            break

    #------------------------------------------------------ 2o erotima

    df2 = pd.read_excel(file_name, usecols='C,K,L,M,N,O,P,Q,R,S,T,U,V') #get columnS c-v 
    #print(df1)
    
    mylist2 = df2.values.tolist() 
    #print(mylist2)

    total_plithismos_over_thirty = []
    for i in mylist2[5:]:
        if 'ΔΗΜΟΤΙΚΗ ΕΝΟΤΗΤΑ' in i[0]:
            s = 0
            for k in range(1,13):
                #print(i[k])
                s+=i[k]
            total_plithismos_over_thirty.append(s)
           
    #total_plithismos_over_thirty.sort()
    #print(total_plithismos_over_thirty)
    athroisma = 0
    for j in total_plithismos_over_thirty:
        athroisma+=j

    mo = athroisma / len(total_plithismos_over_thirty)
    print('o mesos oros einai: ',mo)


#----------------------------------------------------- 3o erotima

    df3 = pd.read_excel(file_name, usecols='C,D') #get column C,D 
    #print(df1)
    
    mylist3 = df3.values.tolist() 
    #print(mylist2)

    l = []
    for i in mylist3[5:]:
        if 'ΔΗΜΟΤΙΚΗ ΕΝΟΤΗΤΑ' in i[0]:
            l.append(int(i[1]))

    l.sort()
    #print(l)

    #print(len(l))

    #typos gia diameso
    if len(l)%2 == 0:
        diam1 = l[int(len(l)/2)]
        diam2 = l[int((len(l))/2)+1]
        diam = (diam1+diam2)/2
        print('h diamesos einai: ',int(diam))
    else:
        diam2 = l[int((len(l)+1)/2)]
        print(diam)

#----------------------------------------------------- 4o erotima

    df4 = pd.read_excel(file_name, usecols='C,D') #get column C,D 
    #print(df1)
    
    mylist4 = df4.values.tolist() 
    #print(mylist2)

    plithismos = []
    for i in mylist4[5:]:
        if 'ΔΗΜΟΣ' in i[0]:
            plithismos.append((i[0],int(i[1])))

    # take second element for sort
    def takeSecond(elem):
        return elem[1]

    plithismos.sort(key=takeSecond)
    plithismos.reverse()
    #print(plithismos)
    g=1
    for i in plithismos:
        print(f'{g} thesh: {i[0]} --- {i[1]}')
        g+=1



open_file()