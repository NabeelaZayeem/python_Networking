import openpyxl as op
import pandas as pd
import xlwings as xlw
class CompareXlSheet():
    def __init__(self):
        pass
    def compare(self,sheet1,sheet2,sh1_name,sh2_name):
        self.sheet1=sheet1
        self.sheet2=sheet2
        self.sh1_name=sh1_name
        self.sh2_name=sh2_name
        self.df1=pd.read_excel(self.sheet1,sheet_name=self.sh1_name)
        self.df2=pd.read_excel(self.sheet2,sheet_name=self.sh2_name)
        self.df3=pd.merge(self.df1,self.df2,how="outer",indicator="Exist")
        print(self.df3.query("Exist!='both'"))
        self.df3.to_excel(".//difff.xlsx")
sheet1_path="..//compare_two_sheets_with_df//Arrival_Dates_df.xlsx"
sheet2_path="..//compare_two_sheets_with_df//Arrival_Dates_Final _df.xlsx"
sheet1_name="Sheet1"
sheet2_name="Sheet2"


obj=CompareXlSheet()
obj.compare(sheet1_path,sheet2_path,sheet1_name,sheet2_name)