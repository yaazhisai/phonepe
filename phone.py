import pandas as pd
import mysql.connector
import json
import os
import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
import locale
from babel import numbers
import plotly.express as pt
# from PIL import Image
import base64

def agg_state_list():
    #This is to direct the path to get the data as states

    path="C:/Users/yaazhisai/Desktop/project2/pulse/data/aggregated/transaction/country/india/state/"
    Agg_state_list=os.listdir(path)
    #Agg_state_list--> to get the list of states in India

    final={'States':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

    for i in Agg_state_list:
        path_i=path+i+'/'
        Agg_year_list=os.listdir(path_i)  # gives all the years present in that state
        for j in Agg_year_list:
            path_j=path_i+j+"/"
            out_js=os.listdir(path_j)
            for k in out_js:
                path_k=path_j+k
                r=open(path_k,'r')
                response=json.load(r)
                for items in response['data']['transactionData']:
                    name=items['name']
                    count=items['paymentInstruments'][0]['count']
                    amount=items['paymentInstruments'][0]['amount']
                    final['Transaction_type'].append(name)
                    final['Transaction_count'].append(count)
                    final['Transaction_amount'].append(amount)
                    final['States'].append(i)
                    final['Year'].append(j)
                    final['Quarter'].append(int(k.strip('.json')))

    final_agg_trans=pd.DataFrame(final)
    
    
    final_agg_trans["States"]=final_agg_trans["States"].str.replace("-"," ")
    final_agg_trans["States"]=final_agg_trans["States"].str.title()
    final_agg_trans["States"]=final_agg_trans["States"].str.replace("&","and")
    final_agg_trans["States"]=final_agg_trans["States"].str.replace("Jammu And Kashmir","Jammu and Kashmir")
    final_agg_trans['States']=final_agg_trans['States'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli")
    final_agg_trans["States"]=final_agg_trans["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
    final_agg_trans["States"]=final_agg_trans["States"].str.replace("Uttarakhand","Uttaranchal")
    final_agg_trans["States"]=final_agg_trans["States"].str.replace("Odisha","Orissa")

    return final_agg_trans
    
def agg_state_user():

    path="C:/Users/yaazhisai/Desktop/project2/pulse/data/aggregated/user/country/india/state/"
    Agg_state_user=os.listdir(path)
    #Agg_state_list--> to get the list of states in India

    brand=""
    count=""

    final1={'States':[], 'Year':[],'Quarter':[],'Num_Rusers':[],'App_open':[],'Brand':[],'Register_brand':[]}

    for i in Agg_state_user:
        path_i=path+i+'/'
        Agg_year_user=os.listdir(path_i)  # gives all the years present in that state
        for j in Agg_year_user:
            path_j=path_i+j+"/"
            out_js=os.listdir(path_j)
            for k1 in out_js:
                path_k=path_j+k1
                r=open(path_k,'r')
                response1=json.load(r)
                #print(response1)
                for k,v in dict.items(response1['data']):
                    if k == 'aggregated':
                        reg_user=v['registeredUsers']
                        #print(reg_user)
                        app_open=v['appOpens']
                        #print(app_open)
                        brand=""
                        count=""
                        final1['States'].append(i)
                        final1['Year'].append(j)
                        final1['Quarter'].append(k1.strip('.json'))
                        final1['Num_Rusers'].append(reg_user)
                        final1['App_open'].append(app_open)
                        final1['Brand'].append(brand)
                        final1['Register_brand'].append(count)
                    elif k=='usersByDevice':
                        if v!=None:
                            for x in v:
                                brand=x['brand']
                                count=x['count']
                                final1['States'].append(i)
                                final1['Year'].append(j)
                                final1['Quarter'].append(k1.strip('.json'))
                                final1['Num_Rusers'].append(reg_user)
                                final1['App_open'].append(app_open)
                                final1['Brand'].append(brand)
                                final1['Register_brand'].append(count)


    final_agg_user=pd.DataFrame(final1)
    final_agg_user["States"]=final_agg_user["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
    final_agg_user["States"]=final_agg_user["States"].str.replace("-"," ")
    final_agg_user["States"]=final_agg_user["States"].str.replace("&","and")
    final_agg_user["States"]=final_agg_user["States"].str.title()
    final_agg_user["States"]=final_agg_user["States"].str.replace("Jammu And Kashmir","Jammu and Kashmir")
    final_agg_user['States']=final_agg_user['States'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli")
    final_agg_user["States"]=final_agg_user["States"].str.replace("Uttarakhand","Uttaranchal")
    final_agg_user["States"]=final_agg_user["States"].str.replace("Odisha","Orissa")

    return final_agg_user

def map_state_list():
    path="C:/Users/yaazhisai/Desktop/project2/pulse/data/map/transaction/hover/country/india/state/"
    Map_state_list=os.listdir(path)

    Map_state_list

    final2={'States':[], 'Year':[],'Quarter':[],'District':[], 'Transacion_count':[], 'Transacion_amount':[]}

    for i in Map_state_list:
        path_i=path+i+"/"
        Map_year_list=os.listdir(path_i)
        for j in Map_year_list:
            path_j=path_i+j+"/"
            Map_year_list=os.listdir(path_j)
            for k in Map_year_list:
                path_k=path_j+k
                r=open(path_k,'r')
                response2=json.load(r)
                response2
                for z in response2['data']['hoverDataList']:
                    district=z['name']
                    trans_count=z['metric'][0]['count']
                    trans_amount=z['metric'][0]['amount']
                    #print(district,trans_count,trans_amount)
                    final2['States'].append(i)
                    final2['Year'].append(j)
                    final2['Quarter'].append(k.strip(".json"))
                    final2['District'].append(district)
                    final2['Transacion_count'].append(trans_count)
                    final2['Transacion_amount'].append(trans_amount)

    final_map_trans=pd.DataFrame(final2)
    final_map_trans["States"]=final_map_trans["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
    final_map_trans["States"]=final_map_trans["States"].str.replace("-"," ")
    final_map_trans["States"]=final_map_trans["States"].str.replace("&","and")
    final_map_trans["States"]=final_map_trans["States"].str.title()
    final_map_trans["States"]=final_map_trans["States"].str.replace("Jammu And Kashmir","Jammu and Kashmir")
    final_map_trans['States']=final_map_trans['States'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli")
    final_map_trans["States"]=final_map_trans["States"].str.replace("Odisha","Orissa")
    final_map_trans["States"]=final_map_trans["States"].str.replace("Uttarakhand","Uttaranchal")

    return final_map_trans

def map_state_user():
    path="C:/Users/yaazhisai/Desktop/project2/pulse/data/map/user/hover/country/india/state/"
    Map_state_user=os.listdir(path)

    Map_state_user

    final3={'States':[], 'Year':[],'Quarter':[],'District':[], 'Reg_user':[], 'Total_appopen':[]}

    for i in Map_state_user:
        path_i=path+i+"/"
        Map_year_user=os.listdir(path_i)
        for j in Map_year_user:
            path_j=path_i+j+"/"
            Map_year_user=os.listdir(path_j)
            for k in Map_year_user:
                path_k=path_j+k
                r=open(path_k,'r')
                response3=json.load(r)
                response3
                for key,val in dict.items(response3['data']['hoverData']):
                    #print(key,val)
                    district=key
                    reg_user=val["registeredUsers"]
                    tapp_open=val["appOpens"]
                    final3['States'].append(i)
                    final3['Year'].append(j)
                    final3['Quarter'].append(k.strip(".json"))
                    final3['District'].append(district)
                    final3['Reg_user'].append(reg_user)
                    final3['Total_appopen'].append(tapp_open)
                    
    final_map_user=pd.DataFrame(final3)
    final_map_user["States"]=final_map_user["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
    final_map_user["States"]=final_map_user["States"].str.replace("-"," ")
    final_map_user["States"]=final_map_user["States"].str.replace("&","and")
    final_map_user["States"]=final_map_user["States"].str.title()
    final_map_user["States"]=final_map_user["States"].str.replace("Jammu And Kashmir","Jammu and Kashmir")
    final_map_user['States']=final_map_user['States'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli")
    final_map_user["States"]=final_map_user["States"].str.replace("Uttarakhand","Uttaranchal")
    final_map_user["States"]=final_map_user["States"].str.replace("Odisha","Orissa")

    return final_map_user

def top_trans_state():
    path="C:/Users/yaazhisai/Desktop/project2/pulse/data/top/transaction/country/india/"
    top_year_list=os.listdir(path)

    top_year_list.remove('state')

    final4_state={'States':[], 'Year':[],'Quarter':[], 'Trans_count':[], 'Total_amount':[]}


    for i in top_year_list:
        path_i=path+i+"/"
        top_out=os.listdir(path_i)
        for k in top_out:
            path_k=path_i+k
            r=open(path_k,'r')
            response4=json.load(r)
            for z in response4['data']['states']:
                state=z['entityName']
                trans_count=z['metric']['count']
                trans_amount=z['metric']['amount']
                final4_state['States'].append(state)
                final4_state['Year'].append(i)
                final4_state['Quarter'].append(k.strip(".json"))
                final4_state['Trans_count'].append(trans_count)
                final4_state['Total_amount'].append(trans_amount)
        
    final_top_transac_state=pd.DataFrame(final4_state)
    final_top_transac_state['States']=final_top_transac_state["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
    final_top_transac_state["States"]=final_top_transac_state["States"].str.replace("-"," ")
    final_top_transac_state["States"]=final_top_transac_state["States"].str.replace("&","and")
    final_top_transac_state["States"]=final_top_transac_state["States"].str.title()
    final_top_transac_state["States"]=final_top_transac_state["States"].str.replace("Jammu And Kashmir","Jammu and Kashmir")
    final_top_transac_state['States']=final_top_transac_state['States'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli")
    final_top_transac_state["States"]=final_top_transac_state["States"].str.replace("Odisha","Orissa")
    final_top_transac_state["States"]=final_top_transac_state["States"].str.replace("Uttarakhand","Uttaranchal")

    return final_top_transac_state

def top_district_list():

    final5_districts={'States':[],'districts':[], 'Year':[],'Quarter':[], 'Trans_count':[], 'Total_amount':[]}
    final6_pincodes={'States':[],'pincodes':[], 'Year':[],'Quarter':[], 'Trans_count':[], 'Total_amount':[]}

    path="C:/Users/yaazhisai/Desktop/project2/pulse/data/top/transaction/country/india/state/"
    top_state_list=os.listdir(path)

    for i in top_state_list:
        path_i=path+i+'/'
        top_year_list=os.listdir(path_i)
        for j in top_year_list:
            path_j=path_i+j+"/"
            top_out=os.listdir(path_j)
            for k in top_out:
                path_k=path_j+k
                r=open(path_k,'r')
                response4=json.load(r)
                for z in response4['data']['districts']:
                    state=i
                    districts=z['entityName']
                    trans_count=z['metric']['count']
                    trans_amount=z['metric']['amount']
                    final5_districts['States'].append(state)
                    final5_districts['districts'].append(districts)
                    final5_districts['Year'].append(j)
                    final5_districts['Quarter'].append(k.strip(".json"))
                    final5_districts['Trans_count'].append(trans_count)
                    final5_districts['Total_amount'].append(trans_amount)
                for z in response4['data']['pincodes']:
                    state=i
                    pincodes=z['entityName']
                    trans_count=z['metric']['count']
                    trans_amount=z['metric']['amount']
                    final6_pincodes['States'].append(state)
                    final6_pincodes['pincodes'].append(pincodes)
                    final6_pincodes['Year'].append(j)
                    final6_pincodes['Quarter'].append(k.strip(".json"))
                    final6_pincodes['Trans_count'].append(trans_count)
                    final6_pincodes['Total_amount'].append(trans_amount)

    
    final_top_transac_districts=pd.DataFrame(final5_districts)
    final_top_transac_districts["States"]=final_top_transac_districts["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
    final_top_transac_districts["States"]=final_top_transac_districts["States"].str.replace("-"," ")
    final_top_transac_districts["States"]=final_top_transac_districts["States"].str.replace("&","and")
    final_top_transac_districts["States"]=final_top_transac_districts["States"].str.title()
    final_top_transac_districts["States"]=final_top_transac_districts["States"].str.replace("Jammu And Kashmir","Jammu and Kashmir")
    final_top_transac_districts['States']=final_top_transac_districts['States'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli")
    final_top_transac_districts["States"]=final_top_transac_districts["States"].str.replace("Odisha","Orissa")
    final_top_transac_districts["States"]=final_top_transac_districts["States"].str.replace("Uttarakhand","Uttaranchal")

    final_top_transac_pincodes=pd.DataFrame(final6_pincodes)
    final_top_transac_pincodes["States"]=final_top_transac_pincodes["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
    final_top_transac_pincodes["States"]=final_top_transac_pincodes["States"].str.replace("-"," ")
    final_top_transac_pincodes["States"]=final_top_transac_pincodes["States"].str.replace("&","and")
    final_top_transac_pincodes["States"]=final_top_transac_pincodes["States"].str.title()
    final_top_transac_pincodes["States"]=final_top_transac_pincodes["States"].str.replace("Jammu And Kashmir","Jammu and Kashmir")
    final_top_transac_pincodes['States']=final_top_transac_pincodes['States'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli")
    final_top_transac_pincodes["States"]=final_top_transac_pincodes["States"].str.replace("Odisha","Orissa")
    final_top_transac_pincodes["States"]=final_top_transac_pincodes["States"].str.replace("Uttarakhand","Uttaranchal")
    
    return final_top_transac_districts, final_top_transac_pincodes

def top_user_list():
    path="C:/Users/yaazhisai/Desktop/project2/pulse/data/top/user/country/india/"
    top_year_user=os.listdir(path)

    top_year_user.remove('state')

    final7_state_user={'States':[], 'Year':[],'Quarter':[], 'Reguser_count':[]}
    
    for i in top_year_user:
        path_i=path+i+"/"
        top_out_user=os.listdir(path_i)
        for k in top_out_user:
            path_k=path_i+k
            r=open(path_k,'r')
            response5=json.load(r)
            for z in response5['data']['states']:
                #print(z)
                state=z['name']
                reg_user=z['registeredUsers']
                final7_state_user['States'].append(state)
                final7_state_user['Year'].append(i)
                final7_state_user['Quarter'].append(k.strip(".json"))
                final7_state_user['Reguser_count'].append(reg_user)
    final_top_user_state=pd.DataFrame(final7_state_user)
    final_top_user_state["States"]=final_top_user_state["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
    final_top_user_state["States"]=final_top_user_state["States"].str.replace("-"," ")
    final_top_user_state["States"]=final_top_user_state["States"].str.replace("&","and")
    final_top_user_state["States"]=final_top_user_state["States"].str.title()
    final_top_user_state["States"]=final_top_user_state["States"].str.replace("Jammu And Kashmir","Jammu and Kashmir")
    final_top_user_state['States']=final_top_user_state['States'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli")
    final_top_user_state["States"]=final_top_user_state["States"].str.replace("Uttarakhand","Uttaranchal")
    final_top_user_state["States"]=final_top_user_state["States"].str.replace("Odisha","Orissa")

    return final_top_user_state

        
def top_user_district():

    final8_districts_user={'States':[],'Districts':[], 'Year':[],'Quarter':[], 'Reguser_count':[]}
    final9_pincodes_user={'States':[],'Pincode':[], 'Year':[],'Quarter':[], 'Reguser_count':[]}

    path="C:/Users/yaazhisai/Desktop/project2/pulse/data/top/user/country/india/state/"
    top_state_list=os.listdir(path)
    for i in top_state_list:
        path_i=path+i+'/'
        top_year_user=os.listdir(path_i)
        for j in top_year_user:
            path_j=path_i+j+"/"
            top_out_user=os.listdir(path_j)
            for k in top_out_user:
                path_k=path_j+k
                r=open(path_k,'r')
                response5=json.load(r)
                for z in response5['data']['districts']:
                    state=i
                    districts=z['name']
                    reg_user=z['registeredUsers']
                    final8_districts_user['States'].append(state)
                    final8_districts_user['Districts'].append(districts)
                    final8_districts_user['Year'].append(j)
                    final8_districts_user['Quarter'].append(k.strip(".json"))
                    final8_districts_user['Reguser_count'].append(reg_user)
                for z in response5['data']['pincodes']:
                    state=i
                    pincodes=z['name']
                    reg_user=z['registeredUsers']
                    final9_pincodes_user['States'].append(state)
                    final9_pincodes_user['Pincode'].append(pincodes)
                    final9_pincodes_user['Year'].append(j)
                    final9_pincodes_user['Quarter'].append(k.strip(".json"))
                    final9_pincodes_user['Reguser_count'].append(reg_user)
                    

    final_top_user_districts=pd.DataFrame(final8_districts_user)

    final_top_user_districts["States"]=final_top_user_districts["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
    final_top_user_districts["States"]=final_top_user_districts["States"].str.replace("-"," ")
    final_top_user_districts["States"]=final_top_user_districts["States"].str.replace("&","and")
    final_top_user_districts["States"]=final_top_user_districts["States"].str.title()
    final_top_user_districts["States"]=final_top_user_districts["States"].str.replace("Jammu And Kashmir","Jammu and Kashmir")
    final_top_user_districts['States']=final_top_user_districts['States'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli")
    final_top_user_districts["States"]=final_top_user_districts["States"].str.replace("Uttarakhand","Uttaranchal")
    final_top_user_districts["States"]=final_top_user_districts["States"].str.replace("Odisha","Orissa")
    
    final_top_user_pincodes=pd.DataFrame(final9_pincodes_user)

    final_top_user_pincodes["States"]=final_top_user_pincodes["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
    final_top_user_pincodes["States"]=final_top_user_pincodes["States"].str.replace("-"," ")
    final_top_user_pincodes["States"]=final_top_user_pincodes["States"].str.replace("&","and")
    final_top_user_pincodes["States"]=final_top_user_pincodes["States"].str.title()
    final_top_user_pincodes["States"]=final_top_user_pincodes["States"].str.replace("Jammu And Kashmir","Jammu and Kashmir")
    final_top_user_pincodes['States']=final_top_user_pincodes['States'].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli")
    final_top_user_pincodes["States"]=final_top_user_pincodes["States"].str.replace("Uttarakhand","Uttaranchal")
    final_top_user_pincodes["States"]=final_top_user_pincodes["States"].str.replace("Odisha","Orissa")
    
    return final_top_user_districts, final_top_user_pincodes

def create_db():
    # Run only once for database and tables creation
    mydb=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
    )
    mycursor=mydb.cursor(buffered=True)     
    mycursor.execute("CREATE DATABASE phonepe")
    mycursor.execute("USE phonepe")
    mycursor.execute("CREATE TABLE agg_trans (state VARCHAR(250),year INT(10),quarter INT(2),trans_type VARCHAR(250),trans_count INT(50),trans_amount FLOAT(50))")
    mycursor.execute("CREATE TABLE agg_user (state VARCHAR(250),year INT(10),quarter INT(2),num_rusers int(50),app_open INT(10),brand VARCHAR(250),reg_brand VARCHAR(250))")
    mycursor.execute("CREATE TABLE map_trans (state VARCHAR(250),year INT(10),quarter INT(10),district VARCHAR(250),trans_count INT(50),trans_amount FLOAT(50))")
    mycursor.execute("CREATE TABLE map_user (state VARCHAR(250),year INT(10),quarter INT(10),districts VARCHAR(250),num_rusers INT(50),app_open INT(50))")
    mycursor.execute("CREATE TABLE top_trans_states (state VARCHAR(250),year INT(10),quarter INT(10),trans_count INT(50),trans_amount FLOAT(50))")
    mycursor.execute("CREATE TABLE top_trans_districts (state VARCHAR(250),districts VARCHAR(250),year INT(10),quarter INT(10),trans_count INT(50),trans_amount FLOAT(50))")
    mycursor.execute("CREATE TABLE top_trans_pincodes (state VARCHAR(250),pincodes VARCHAR(250),year INT(10),quarter INT(10),trans_count INT(50),trans_amount FLOAT(50))")
    mycursor.execute("CREATE TABLE top_user_states (states VARCHAR(250),year INT(10),quarter INT(10),num_rusers INT(50))")
    mycursor.execute("CREATE TABLE top_user_districts(state VARCHAR(250),districts VARCHAR(250),year INT(10),quarter INT(10),num_rusers INT(50))")
    mycursor.execute("CREATE TABLE top_user_pincodes(state VARCHAR(250),pincodes VARCHAR(250),year INT(10),quarter INT(10),num_rusers INT(50))")

    mydb.commit()

def table_insert():
    mydb=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
    )
    mycursor=mydb.cursor(buffered=True)     
    mycursor.execute("USE phonepe")

    query1="INSERT INTO agg_trans (state,year,quarter,trans_type,trans_count,trans_amount) values(%s,%s,%s,%s,%s,%s)"
    final_agg_trans = agg_state_list()
    val=final_agg_trans.values.tolist()
    mycursor.executemany(query1,val)
    mydb.commit()

    query2="INSERT INTO agg_user(state,year,quarter,num_rusers,app_open,brand,reg_brand) values(%s,%s,%s,%s,%s,%s,%s)"
    final_agg_user = agg_state_user()
    val=final_agg_user.values.tolist()
    mycursor.executemany(query2,val)
    mydb.commit()

    query3="INSERT INTO map_trans(state,year,quarter,district,trans_count,trans_amount) values(%s,%s,%s,%s,%s,%s)"
    final_map_trans = map_state_list()
    val=final_map_trans.values.tolist()
    mycursor.executemany(query3,val)
    mydb.commit()

    query4="INSERT INTO map_user(state,year,quarter,districts,num_rusers,app_open) values(%s,%s,%s,%s,%s,%s)"
    final_map_user = map_state_user()
    val=final_map_user.values.tolist()
    mycursor.executemany(query4,val)
    mydb.commit()

    query5="INSERT INTO top_trans_states(state,year,quarter,trans_count,trans_amount) values(%s,%s,%s,%s,%s)"
    final_top_transac_state= top_trans_state()
    val=final_top_transac_state.values.tolist()
    mycursor.executemany(query5,val)
    mydb.commit()

    query6="INSERT INTO top_trans_districts(state,districts,year,quarter,trans_count,trans_amount) values(%s,%s,%s,%s,%s,%s)"
    final_top_transac_district, final_top_trans_pincode=top_district_list()
    val=final_top_transac_district.values.tolist()
    mycursor.executemany(query6,val)
    mydb.commit()

    query7="INSERT INTO top_trans_pincodes(state,pincodes,year,quarter,trans_count,trans_amount) values(%s,%s,%s,%s,%s,%s)"
    # final_top_trans_pincode=top_district_list()
    val=final_top_trans_pincode.values.tolist()
    mycursor.executemany(query7,val)
    mydb.commit()

    query8="INSERT INTO top_user_states(states,year,quarter,num_rusers) values(%s,%s,%s,%s)"
    final_top_user_state= top_user_list()
    val=final_top_user_state.values.tolist()
    mycursor.executemany(query8,val)
    mydb.commit()

    query9="INSERT INTO top_user_districts(state,districts,year,quarter,num_rusers) values(%s,%s,%s,%s,%s)"
    final_top_user_districts, final_top_user_pincodes=top_user_district()
    val=final_top_user_districts.values.tolist()
    mycursor.executemany(query9,val)
    mydb.commit()

    query10="INSERT INTO top_user_pincodes(state,pincodes,year,quarter,num_rusers) values(%s,%s,%s,%s,%s)"
    # final_top_user_pincodes=top_user_district()
    val=final_top_user_pincodes.values.tolist()
    mycursor.executemany(query10,val)
    mydb.commit()

def trans(c1,r1,y,q,c4):
    mydb=mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
        )
    mycursor=mydb.cursor(buffered=True)     
    mycursor.execute("USE phonepe")
    
    if c1=='TRANSACTION':
        if r1=='AGGREGATE':
            mycursor.execute("SELECT * from agg_trans")
        elif r1=="MAP":
            mycursor.execute("SELECT * from map_trans")
        elif r1=="TOP_STATE":
            mycursor.execute("SELECT * from top_trans_states")
        elif r1=="TOP_PINCODE":
            mycursor.execute("SELECT * from top_trans_pincodes")
    elif c1=='USER':
        if r1=='AGGREGATE':
            mycursor.execute("SELECT * from agg_user")
        elif r1=="MAP":
            mycursor.execute("SELECT * from map_user")
        elif r1=="TOP_STATE":
            mycursor.execute("SELECT * from top_user_states")
        elif r1=="TOP_DISTRICT":
            mycursor.execute("SELECT * from top_user_districts")
        elif r1=="TOP_PINCODE":
            mycursor.execute("SELECT * from top_user_pincodes")
    
    f1=mycursor.fetchall()
    data_df=pd.DataFrame(f1,columns=mycursor.column_names)
    filbyyear=data_df[data_df['year']==y]
    filbyyear.reset_index(drop=True,inplace=True)
    filbyquar=filbyyear[filbyyear['quarter']==q]
    filbyquar.reset_index(drop=True,inplace=True)
    if c1=="TRANSACTION" and (r1=='AGGREGATE' or r1=='MAP' or r1=='TOP_STATE'):
        out=filbyquar.groupby('state')[['trans_amount','trans_count']].sum() 
        out.reset_index(inplace=True)
        out1=out.sort_values("trans_amount",ascending=False).head(10)
        out1.reset_index(drop=True,inplace=True)
        out2=out.sort_values("trans_count",ascending=False).head(10)
        out2.reset_index(drop=True,inplace=True)
        col1,col2=st.columns(2)
        with col1:
            bar1_amt=pt.bar(out1,x='state',y='trans_amount',title=f"{r1} {y} Q{q} TRANS_AMOUNT",height=450,width=300)
            st.plotly_chart(bar1_amt)
        with col2:
            bar1_count=pt.bar(out2,x='state',y='trans_count',title=f"{r1} {y} Q{q} TRANS_COUNT",height=450,width=300)
            st.plotly_chart(bar1_count)
        
        if c4:
            get_trans_map(out)
    
    
    if c1=="TRANSACTION" and r1=='TOP_PINCODE':
        out=filbyquar.groupby('pincodes')[['trans_amount','trans_count']].sum() 
        out.reset_index(inplace=True)
        out1=out.sort_values("trans_amount",ascending=False).head(10)
        out1.reset_index(drop=True,inplace=True)
        col1,col2=st.columns(2)
        with col1:
            bar1_amt=pt.bar(out1,x='pincodes',y='trans_amount',title=f"{c1} {r1} {y} QUARTER{q}  TRANS_AMOUNT",height=450,width=300)
            st.plotly_chart(bar1_amt)
        with col2:
            bar1_count=pt.bar(out1,x='pincodes',y='trans_count',title=f"{c1} {r1} {y} QUARTER{q} TRANS_COUNT",height=450,width=300)
            st.plotly_chart(bar1_count)
        
        if c4:
            get_trans_map(out)

    if c1=='USER' and r1=='AGGREGATE':
        out=filbyquar.groupby('state')[['num_rusers','reg_brand']].sum()
        out.reset_index(inplace=True)
        out1=out.sort_values("num_rusers",ascending=False).head(10)
        out1.reset_index(drop=True,inplace=True)

        out2=filbyquar.groupby('brand')[['reg_brand']].sum()
        out2.reset_index(inplace=True)
        # print(out2)
        out3=out2.sort_values("reg_brand",ascending=False).head(10)
        out3.reset_index(drop=True,inplace=True)
        # print(out3)
        col1,col2=st.columns(2)
        with col1:
            pie_agg=pt.pie(out1,values='num_rusers',title=f"{c1} {r1} {y} Q{q} USERCOUNT", names='state',height=450,width=350)
            st.plotly_chart(pie_agg)
        with col2:
            pie_agg=pt.pie(out3,values='reg_brand',title=f"{c1} {r1} {y} Q{q} REGBRAND",names='brand',height=450,width=350)
            st.plotly_chart(pie_agg)
        if c4:
            get_user_map(out)


    
    elif c1=='USER' and r1=='MAP':
        out=filbyquar.groupby('state')[['num_rusers','app_open']].sum()
        out.reset_index(inplace=True)
        out1=out.sort_values("num_rusers",ascending=False).head(10)
        out1.reset_index(drop=True,inplace=True)
        col1,col2=st.columns(2)
        with col1:
            pie_agg=pt.pie(out1,values='num_rusers',title=f"{c1} {r1} {y} QUARTER{q} USERCOUNT",names='state',height=450,width=350)
            st.plotly_chart(pie_agg)
        with col2:
            pie_agg=pt.pie(out1,values='app_open',title=f"{c1} {r1} {y} QUARTER{q} APPOPEN",names='state',height=450,width=350)
            st.plotly_chart(pie_agg)
        if c4:
            get_user_map(out)
    elif c1=='USER' and r1=='TOP_STATE':
        out=filbyquar.groupby('states')[['num_rusers']].sum()
        out.reset_index(inplace=True)
        out1=out.sort_values("num_rusers",ascending=False).head(10)
        out1.reset_index(drop=True,inplace=True)
        pie_agg=pt.pie(out1,values='num_rusers',title=f"{c1} {r1} {y} Q{q} USERCOUNT",names='states',height=450,width=300)
        st.plotly_chart(pie_agg)
        if c4:
            get_user_map(out)
    elif c1=='USER' and r1=='TOP_DISTRICT':
        out=filbyquar.groupby('districts')['num_rusers'].sum()
        out.reset_index(inplace=True)
        out1=out.sort_values("num_rusers",ascending=False).head(10)
        out1.reset_index(drop=True,inplace=True)
        pie_agg=pt.pie(out1,values='num_rusers',title=f"{c1} {r1} {y} QUARTER{q} USERCOUNT",names='districts',height=450,width=300)
        st.plotly_chart(pie_agg)
        if c4:
            get_user_map(out)
    elif c1=='USER' and r1=='TOP_PINCODES':
        out=filbyquar.groupby('pincodes')['num_rusers'].sum()
        out.reset_index(inplace=True)
        out1=out.sort_values("num_rusers",ascending=False).head(10)
        out1.reset_index(drop=True,inplace=True)
        col1,col2=st.columns(2)
        with col1:
            pie_agg=pt.pie(out1,values='num_rusers',title=f"{c1} {r1} {y} QUARTER{q} USERCOUNT",names='states',height=450,width=300)
            st.plotly_chart(pie_agg)
        # with col2:
        #     pie_agg=pt.pie(out2,values='reg_brand',names='brand')
        #     st.plotly_chart(pie_agg)
        if c4:
            get_user_map(out)

def top_dist(c1,r1,y,q,c4,s1):
    mydb=mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
        )
    mycursor=mydb.cursor(buffered=True)     
    mycursor.execute("USE phonepe")

    if c1=='TRANSACTION':
        if r1=="TOP_DISTRICT":
            mycursor.execute("SELECT * from top_trans_districts")
        if r1=='TOP_PINCODE':
            mycursor.execute("SELECT * from top_trans_pincodes")
    elif c1=="USER":
        if r1=="TOP_DISTRICT":
            mycursor.execute("SELECT * from top_user_districts")
        if r1=='TOP_PINCODE':
            mycursor.execute("SELECT * from top_user_pincodes")
        

    f1=mycursor.fetchall()
    data_df=pd.DataFrame(f1,columns=mycursor.column_names)

    filbystate=data_df[data_df['state']==s1]
    filbystate.reset_index(drop=True,inplace=True)
    filbyyear=filbystate[filbystate['year']==y]
    filbyyear.reset_index(drop=True,inplace=True)
    filbyquar=filbyyear[filbyyear['quarter']==q]
    filbyquar.reset_index(drop=True,inplace=True)

    if c1=="TRANSACTION" and r1=='TOP_DISTRICT':
        out=filbyquar.groupby('districts')[['trans_amount','trans_count']].sum() 
        out.reset_index(inplace=True)
        
        out1=out.sort_values("trans_amount",ascending=False).head(10)
        out1.reset_index(drop=True,inplace=True)
        col1,col2=st.columns(2)
        with col1:
            bar1_amt=pt.bar(out1,x='districts',y='trans_amount',title=f"10{r1} {y} Q{q} TRANS_AMOUNT",height=450,width=300)
            st.plotly_chart(bar1_amt)
        with col2:
            bar1_count=pt.bar(out1,x='districts',y='trans_count',title=f"10{r1} {y} Q{q} TRANS_COUNT",height=450,width=300)
            st.plotly_chart(bar1_count)

    if c1=="TRANSACTION" and r1=='TOP_PINCODE':
        out=filbyquar.groupby('pincodes')[['trans_amount','trans_count']].sum() 
        out.reset_index(inplace=True)
        out1=out.sort_values("trans_amount",ascending=False).head(10)
        out1.reset_index(drop=True,inplace=True)
        col1,col2=st.columns(2)
        with col1:
            #bar1_amt=pt.bar(out1,x='pincodes',y='trans_amount',title=f"{c1} {r1} {y} Q{q}  TRANS_AMOUNT",height=450,width=300)
            #st.plotly_chart(bar1_amt)
            pie_agg=pt.pie(out1,values='trans_amount',title=f"{r1} {y} Q{q} TRANS_AMOUNT", names='pincodes',height=450,width=300)
            st.plotly_chart(pie_agg)
        with col2:
            pie_agg=pt.pie(out1,values='trans_count',title=f"{r1} {y} Q{q} TRANS_COUNT", names='pincodes',height=450,width=300)
            st.plotly_chart(pie_agg)
        
    if c1=="USER" and r1=='TOP_DISTRICT':
        out=filbyquar.groupby('districts')[['num_rusers']].sum() 
        out.reset_index(inplace=True)        
        out1=out.sort_values("num_rusers",ascending=False).head(10)
        out1.reset_index(drop=True,inplace=True)
        pie_agg=pt.pie(out1,values='num_rusers',title=f"{r1} {y} Q{q} USERCOUNT", names='districts',height=450,width=300)
        st.plotly_chart(pie_agg)
    if c1=="USER" and r1=='TOP_PINCODE':
        out=filbyquar.groupby('pincodes')[['num_rusers']].sum() 
        out.reset_index(inplace=True)
        out1=out.sort_values("num_rusers",ascending=False).head(10)
        out1.reset_index(drop=True,inplace=True)
        pie_agg=pt.pie(out1,values='num_rusers',title=f"{r1} {y} Q{q} USER_COUNT", names='pincodes',height=450,width=300)
        st.plotly_chart(pie_agg)
        
def trans_cat(c1,r1,y,q):
    mydb=mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
        )
    mycursor=mydb.cursor(buffered=True)     
    mycursor.execute("USE phonepe")

    if c1=='TRANSACTION' and r1=='CATEGORIES':
        mycursor.execute("select * from agg_trans")

    f1=mycursor.fetchall()
    data_df=pd.DataFrame(f1,columns=mycursor.column_names)

    filbyyear=data_df[data_df['year']==y]
    filbyyear.reset_index(drop=True,inplace=True)
    filbyquar=filbyyear[filbyyear['quarter']==q]
    filbyquar.reset_index(drop=True,inplace=True)

    out=filbyquar.groupby(['trans_type','year','quarter'])[['trans_amount']].sum() 
    out.reset_index(inplace=True)        
    out1=out.sort_values("trans_amount",ascending=False)
    out1.reset_index(drop=True,inplace=True)

    out2=filbyquar.groupby(['trans_type','year','quarter'])[['trans_count']].sum() 
    out2.reset_index(inplace=True)        
    out3=out2.sort_values("trans_count",ascending=False)
    out3.reset_index(drop=True,inplace=True)
    # st.write(out1)
    # st.write(out3)
    col1,col2=st.columns(2)
    with col1:
        bar1_amt=pt.bar(out1,x='trans_type',y='trans_amount',title=f"{r1} {y} Q{q} TRANS_AMOUNT",height=450,width=300)
        st.plotly_chart(bar1_amt)
    with col2:
        bar1_amt=pt.bar(out3,x='trans_type',y='trans_count',title=f"{r1} {y} Q{q} TRANS_COUNT",height=450,width=300)
        st.plotly_chart(bar1_amt)

        
def get_trans_map(df):
    
    map=folium.Map(location=(20.5937,78.9629),zoom_start=4, scrollWheelZoom=False,titles='cartoDB positron')
    choropleth=folium.Choropleth(
        geo_data="C:/Users/yaazhisai/Desktop/project2/india_state_geo.json",
        data=df,
        columns=('state','trans_amount'),
        key_on="feature.properties.NAME_1",
        fill_color="RdYlGn_r",
        fill_opacity=0.8,
        line_opacity=0.3,
        highlight=True 
    )
    choropleth.geojson.add_to(map)

    # looping thru the geojson object and adding a new property(trans_amount)
    # and assigning a value from our dataframe
    locale.setlocale(locale.LC_MONETARY, 'en_IN')
    for s in choropleth.geojson.data['features']:
        s['properties']['trans_amount'] = locale.currency(df[df['state']==s['properties']['NAME_1']]['trans_amount'].sum(),grouping=True)
        # float conversion reqd as it was hitting json encode error
        s['properties']['trans_count'] = numbers.format_decimal(float(df[df['state']==s['properties']['NAME_1']]['trans_count'].sum()),locale='en_IN')

    tooltip = folium.GeoJsonTooltip(
                fields=['NAME_1','trans_amount','trans_count'], labels=True, 
                aliases=['State','Transaction Amount','Transaction Count'],
                max_width=1000)
    choropleth.geojson.add_child(tooltip)

    st.title("GEO MAP")
    st_map=st_folium(map,width=700, height=450)

def get_user_map(df):
    
    map=folium.Map(location=(20.5937,78.9629),zoom_start=4, scrollWheelZoom=False,titles='cartoDB positron')
    choropleth=folium.Choropleth(
        geo_data="C:/Users/yaazhisai/Desktop/project2/india_state_geo.json",
        data=df,
        columns=('state','num_rusers'),
        key_on="feature.properties.NAME_1",
        fill_color="RdYlGn_r",
        fill_opacity=0.8,
        line_opacity=0.3,
        highlight=True 
    )
    choropleth.geojson.add_to(map)

    # looping thru the geojson object and adding a new property(trans_amount)
    # and assigning a value from our dataframe
    locale.setlocale(locale.LC_MONETARY, 'en_IN')
    for s in choropleth.geojson.data['features']:
        #s['properties'][''] = locale.currency(df[df['state']==s['properties']['NAME_1']]['trans_amount'].sum(),grouping=True)
        # float conversion reqd as it was hitting json encode error
        s['properties']['num_rusers'] = numbers.format_decimal(float(df[df['state']==s['properties']['NAME_1']]['num_rusers'].sum()),locale='en_IN')

    tooltip = folium.GeoJsonTooltip(
                fields=['NAME_1','num_rusers'], labels=True, 
                aliases=['State','RegUserCount'],
                max_width=1000)
    choropleth.geojson.add_child(tooltip)

    st.title("GEO MAP")
    st_map=st_folium(map,width=700, height=450)

st.image("y.jpg", use_column_width="always", width=700)

# create_db()
# table_insert()

# Sidebar selection window
# icon = Image.open("C:/Users/yaazhisai/Desktop/project2/y.jpg")   

st.markdown(f'<h1 style="text-align: center;">PhonePe Pulse Data Visualization \
            and Exploration</h1>', unsafe_allow_html=True)
c1=st.sidebar.selectbox("SELECT TYPE",(" ","TRANSACTION","USER"))
if c1!=" ":
    if c1!="USER":
        r1=st.sidebar.radio("SELECT TRANSACTION TYPE:",["AGGREGATE","MAP",'CATEGORIES',"TOP_STATE","TOP_DISTRICT","TOP_PINCODE"])
    else:
        r1=st.sidebar.radio("SELECT TRANSACTION TYPE:",["AGGREGATE","MAP","TOP_STATE","TOP_DISTRICT","TOP_PINCODE"])
    if r1=="AGGREGATE" or r1=='MAP' or r1=='TOP_STATE':
        c2=st.sidebar.selectbox("YEAR",(" ",2018,2019,2020,2021,2022,2023))
        c3=st.sidebar.selectbox("QUARTER",(" ","Q1","Q2","Q3","Q4"))
        if c2!=" " and c3!=" ":
            c3=c3[1:2]
            if r1=="AGGREGATE" or r1=="MAP":
                c4=st.sidebar.checkbox("Check for GEO Map")
            else:
                c4=False
            trans(c1,r1,int(c2),int(c3),c4)

    elif r1=='TOP_PINCODE' or r1=='TOP_DISTRICT':
        s1=st.sidebar.selectbox('CHOOSE THE STATE:',(" ","Andaman and Nicobar","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Orissa","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Tripura","Uttar Pradesh","Uttaranchal","West Bengal"))
        c2=st.sidebar.selectbox("YEAR",(" ",2018,2019,2020,2021,2022,2023))
        c3=st.sidebar.selectbox("QUARTER",(" ","Q1","Q2","Q3","Q4"))
        if s1!=" " and c2!=" " and c3!=" ":
            c3=c3[1:2]            
            c4=False
            top_dist(c1,r1,int(c2),int(c3),c4,s1)

    elif r1=='CATEGORIES':
        #category=st.sidebar.selectbox("TRANSACTION CATEGORIES",['Recharge & bill payments',"Peer-to-peer payments",'Merchant payments','Financial Services','Others'])
        c2=st.sidebar.selectbox("YEAR",(" ",2018,2019,2020,2021,2022,2023))
        c3=st.sidebar.selectbox("QUARTER",(" ","Q1","Q2","Q3","Q4"))
        if c2!=" " and c3!=" ":
            c3=c3[1:2]
            trans_cat(c1,r1,int(c2),int(c3))

