import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

data=pd.read_csv('country_wise_latest.csv')
print(data.info())

def daily_cases(data):
    d=data.get("New cases")
    dic={"Terminal":1,"Plot":2}
    print(dic)
    inp=int(input("Terminal/plot (1/2): "))
    cases=[]
    country=[]
    for i in data.get("Country/Region"):
        country.append(i)
    for i in data.get("New cases"):
        cases.append(i)
    if(inp==1):
        dp=data.get(["Country/Region","New cases"])
        print(dp.to_string())
       
    elif(inp==2):
        daily_plot(country,cases)
    else:
        print("wrong input\n")
        daily_cases(data)
    
def daily_plot(country,cases):
    countries=[]
    cases1=np.array(cases)
    avg=np.mean(cases1)
    for i in range(0,len(cases)):
        if(cases[i]>=avg):
            countries.append(country[i])
    plt.pie(cases1[cases1>=avg],labels=countries)
    plt.title("Daily Cases")
    plt.show()


def compare_places(data):
    inp=int(input("How many places you want to compare:"))
    index=0
    l=[]
    country=[]
    deaths=[]
    fresh_country=[]
    fresh_deaths=[]
    for i in data.get("Deaths"):
        deaths.append(i)
    for i in range(0,inp):
        l.append(input("Enter the country:"))
    for i in data.get("Country/Region"):
        country.append(i)
    for i in range(0,len(l)):
        if(l[i] in country):
            index=country.index(l[i])
            fresh_country.append(l[i])
            fresh_deaths.append(deaths[index])
    compared_countries_plot(fresh_country,fresh_deaths)
def compared_countries_plot(fc,fd):
    plt.plot(fc,fd,marker="o",color="red")
    plt.title("Deaths in Various countries")
    plt.show()

def avg_place(data):
    country=[]
    deaths=[]
    recovery=[]
    data1=data.get("Country/Region")
    data2=data.get("Deaths")
    data3=data.get("Recovered")
    for i in range(0,len(data1)):
        country.append(data1[i])
        deaths.append(int(data2[i]))
        recovery.append(int(data3[i]))
    inp=input("Enter the country you want avg of:")
    if(inp in country):
        for i in range(0,len(country)):
            d=deaths[i]
            r=recovery[i]
            index=country.index(inp)
            print(f"Given format: country:{country[country.index(inp)]} and avg deaths/ recovery ratio:{deaths[index]/recovery[index]:.2f}")
            avg_place_plot(country[country.index(inp)],deaths[index],recovery[index])
            break
    else:
        print("invalid input\n")
        avg_place(data)
        
def avg_place_plot(c,d,r):
    dta=[]
    dta.append(d)
    dta.append(r)
    plt.pie(dta,labels=["deaths","recovery"])
    plt.title("Pie chart of average of a place")
    plt.show()
    
                
    
def main(data):
    dic={"daily_cases":1,"compare_places":2,"avg_place":3}
    print(dic)
    inp=int(input("Enter the value"))
    if(inp==1):
        daily_cases(data)
    elif(inp==2):
        compare_places(data)
    elif(inp==3):
        avg_place(data)
    else:
        print("Wrong input!!!\n")
        main(data)

main(data)