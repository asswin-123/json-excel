import conversion_modules

if __name__ == "__main__":
    
    path = str(input("Path of JSON file :"))
    sheetname  = str(input("Name of sheet (optional) :"))
    output_file = str(input("Path of Output Excel :"))
    if(sheetname == ""):
        sheetname = "sheet1"
    conversion_modules.json_toXlsx(path,output_file,sheetname)
    
    
