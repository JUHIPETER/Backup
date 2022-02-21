import mysql.connector
import pandas as pd
from datetime import datetime
import re
import numpy as np
import os

def db_connection():
    
    """
    Method : database connection
    input  : --
    output : return database connection object
    """  
    
    try:
        
        mydb = mysql.connector.connect(
        host="fdcl-mysqldb01.mysql.database.azure.com",
        user="fdcldbadmin@fdcl-mysqldb01",
        password="De@m2n!6tor20",
        port="3306",
        database="whc_formulary")
        
        print("Yay database connect sucessfully!!!")

        return mydb

    except Exception as e:

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        error = "Exception on db_connection"+" | "+str(exc_type)+" | "+ str(fname) +" | "+ str(exc_tb.tb_lineno)+" | "
        print(error)
        exit("****************Unable to connect database*****************")

# Database connection
my_db=db_connection()
mycursor = my_db.cursor()  

def insert_data(df2):
    sql = """INSERT INTO formulary_raw_data (

    scraper_id,
    BNF_Chapter_Key,
    BNF_Section_Key,
    BNF_Paragraph_Key,
    Brand_Name,
    Nice_Tag,
    Nice_Tag_Links,
    Formulary_Status,
    Traffic_Light,
    Traffic_Light_Desc,
    Drug_Type,
    Formulary_Type,
    Document_Flag,
    Data_Status,
    created_date,
    created_by,
    Drug_Presentation_raw,
    Organisation_name,
    Source_of_data,
    Additional_Product_Information,
    BNF_Chapter,
    BNF_Section,
    BNF_Paragraph,
    Drug_Presentation,
    Mapping_Data,
    NHS_Code,
    Formulary_Name,
    Indication,
    Drug_Name_Raw,
    Brand_Ratio,

    Comments,
    QC_Status,
    Multiple_RAG,
    Source_Type,
    Source_Schedule_Tracker,
    File_Name
        
    ) 

    VALUES

    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"""
    drugs_clean=[]
    drugs_clean  = [i.lower().strip() for i in drugs_clean if i]

    count=0

    for i in range (len(df2)):
        
        
        if  str(df2['Drug_Name_Raw'][i].lower()) not in drugs_clean :
            
            
            scraper_id=str(df2['scraper_id'][i])
        
            BNF_Chapter_Key=df2['BNF_Chapter_Key'][i]
            
            BNF_Section_Key=df2['BNF_Section_Key'][i]
            
            BNF_Paragraph_Key=df2['BNF_Paragraph_Key'][i]
            
            Brand_Name=df2['Brand_Name'][i]
            Brand_Name=re.sub('[^A-Za-z0-9\s\|\_/\\.\_\-\,\%]+', '', Brand_Name)
            Brand_Name=Brand_Name.strip()
    
            
            Nice_Tag=df2['Nice_Tag'][i]
            
            Nice_Tag_Links=df2['Nice_Tag_Links'][i]
            
            
            
            Formulary_Status=df2['Formulary_Status'][i]
            Formulary_Status=re.sub('[^A-Za-z0-9\s\|\_/\\.\_\-\,\%]+', '', Formulary_Status)
            Formulary_Status=Formulary_Status.strip()
            
            Traffic_Light=df2['Traffic_Light'][i]
            Traffic_Light=re.sub('[^A-Za-z0-9\s\|\_/\\.\_\-\,\%]+', '', Traffic_Light)
            Traffic_Light=Traffic_Light.strip()
            
            Traffic_Light_Desc=df2['Traffic_Light_Desc'][i]
            Traffic_Light_Desc=re.sub('[^A-Za-z0-9\s\|\_/\\.\_\-\,\%]+', '', Traffic_Light_Desc)
            Traffic_Light_Desc=Traffic_Light_Desc.strip()
            
            
            Drug_Type=str(df2['Drug_Type'][i])
            Drug_Type =re.sub('[^A-Za-z0-9\s\|\_/\\.\_\-\,\%]+', '', Drug_Type)
            Drug_Type=Drug_Type.strip()
            
            Formulary_Type=df2['Formulary_Type'][i]
            
            Document_Flag=df2['Document_Flag'][i]
            
            Data_Status=df2['Data_Status'][i]
            
            created_date=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            
            created_by=df2['created_by'][i]
            
            Drug_Presentation_raw=str(df2['Drug_Presentation_raw'][i])
            Drug_Presentation_raw=re.sub('[^A-Za-z0-9\s\|\_/\\.\_\-\,\%\:\(\)]+', '', Drug_Presentation_raw)
            Drug_Presentation_raw=Drug_Presentation_raw.strip()
            
            Organisation_name=df2['Organisation_name'][i]
            
            Source_of_data=df2['Source_of_data'][i]
            
            Additional_Product_Information=str(df2['Additional_Product_Information'][i])
            Additional_Product_Information=re.sub('[^A-Za-z0-9\s\|\_/\\.\_\-\,\%\:\(\)]+', '', Additional_Product_Information)
            Additional_Product_Information=Additional_Product_Information.strip()
            
            
            BNF_Chapter=df2['BNF_Chapter'][i]
            
            BNF_Section=df2['BNF_Section'][i]
            
            BNF_Paragraph=df2['BNF_Paragraph'][i]
            
            
            if BNF_Chapter == '':
                BNF_Chapter=''
            else:
                BNF_Chapter=int(BNF_Chapter)
                
                
            if BNF_Section == '':
                BNF_Section=''
            else:
                BNF_Section=int(BNF_Section)  
                

            if BNF_Paragraph == '':
                BNF_Paragraph=''
            else:
                BNF_Paragraph=int(BNF_Paragraph)   
            
            
            Drug_Presentation=str(df2['Drug_Presentation'][i])
            Drug_Presentation=re.sub('[^A-Za-z0-9\s\|\_/\\.\_\-\,\%\:\(\)]+', '', Drug_Presentation)
            Drug_Presentation=Drug_Presentation.strip()
            
            Mapping_Data=df2['Mapping_Data'][i]
            
            NHS_Code=df2['NHS_Code'][i]
            
            Formulary_Name=df2['Formulary_Name'][i]
        
            Indication=str(df2['Indication'][i])
            Indication=re.sub('[^A-Za-z0-9\s\|\_/\\.\_\-\,\%\:\(\)]+', '', Indication)
            Indication=Indication.strip()
            
            Drug_Name_Raw=str(df2['Drug_Name_Raw'][i])
            Drug_Name_Raw=re.sub('[^A-Za-z0-9\s\|\_/\\.\_\-\,\%\:\(\)]+', '', Drug_Name_Raw)
            Drug_Name_Raw=Drug_Name_Raw.strip()
            
            Brand_Ratio=df2['Brand_Ratio'][i]
            
            #Mapping_status=df2['Mapping_status'][i]
            
            Comments=df2['Comments'][i]
            
            QC_Status=df2['QC_Status'][i]
            
            Multiple_RAG=df2['Multiple_RAG'][i]
            
            Source_Type=df2['Source_Type'][i]
            
            Source_Schedule_Tracker=df2['source_schedule_tracker'][i]
            
            File_Name=df2['File_Name'][i]
            
    #         Organisation_name="[{'F_name':"+ "'"+Formulary_Name+ "'" + ",'Org Name':"+ "'"+Organisation_name+ "'" + ",'NHSCode':"+ "'"+ str(NHS_Code)+"'" +"}]"
            
            val = (
                
                scraper_id,
                BNF_Chapter_Key,
                BNF_Section_Key,
                BNF_Paragraph_Key,
                Brand_Name,
                Nice_Tag,
                Nice_Tag_Links,
                Formulary_Status,
                Traffic_Light,
                Traffic_Light_Desc,
                Drug_Type,
                Formulary_Type,
                Document_Flag,
                Data_Status,
                created_date,
                created_by,
                Drug_Presentation_raw,
                Organisation_name,
                Source_of_data,
                Additional_Product_Information,
                BNF_Chapter,
                BNF_Section,
                BNF_Paragraph,
                Drug_Presentation,
                Mapping_Data,
                NHS_Code,
                Formulary_Name,
                Indication,
                Drug_Name_Raw,
                Brand_Ratio,
                
                Comments,
                QC_Status,
                Multiple_RAG,
                Source_Type,
                Source_Schedule_Tracker,
                File_Name
                
                )
                    
            mycursor.execute(sql, val)
            my_db.commit()

            print(mycursor.rowcount, "record inserted.")
            count=count+1
            print(count)

def close_connection():
    mycursor.close()
    my_db.close()


if __name__ == "__main__":
    
    
    file_name="missing_RAG_Feb_2022.xlsx"
    isFile = os.path.isfile(file_name)
    if isFile == False:
        sys.exit("************File missisng: Input file is not available in the path************") 
    df = pd.read_excel(file_name)
    df = df.replace(np.nan, '', regex=True)
    df = df.replace('\n',' ', regex=True)
    insert_data(df)
    close_connection()