import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import sys

FILE_Category="Star.csv"


def fetchCSV():
    df1 = pd.read_csv(FILE_Category, index_col="ID")
    return df1

def writeCSV(df):
    df.to_csv(FILE_Category,na_rep = "NULL")

def showCSV(df):
    print (df)

def showLinePlot(df):
    print("line plot")
    x1=df["Category"]
    y1=df['Price'] 
    plt.title("All Records")
    plt.xlabel("Category of Record")
    plt.ylabel("Price of Record")
    plt.plot(x1,y1,marker="*",linestyle=":", linewidth=3,color="red",markersize=10)
    plt.tight_layout()

    # Save the plot to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    # Encode the image stream to base64 for HTML rendering
    lineplot = base64.b64encode(image_stream.read()).decode('utf-8')
    plt.close()  # Close the plot to release resources

    return lineplot

def showBarPlot(df):
    print("bar plot")
    x=df['Brand']
    print(df)
    plt.xlabel('Brand')
    y=df['Quantity']
    plt.bar(x,y,color='red', width=0.5)
    plt.ylabel('Quantity')
    plt.title("Stock details")
    plt.tight_layout()

    # Save the plot to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    # Encode the image stream to base64 for HTML rendering
    barplot = base64.b64encode(image_stream.read()).decode('utf-8')
    plt.close()  # Close the plot to release resources

    return barplot

def addNewshoe(df):
    Brand= input("Enter Brand: ") 
    Category = input("Enter Category: ")
    Itemid=int(input("Enter ITEM ID: ")) 
    Price = int(input("Enter Price: "))
    Quantity = int(input("Enter Quantity: "))
    df.loc[Itemid, :] = [Brand, Category, Quantity, Price]
    print (df) 
    writeCSV(df)

def shoeDetail(df, Itemid): 
    detail = df.loc[Itemid,:]
    print("Details of shoe with item id ", Itemid," is:")
    print(detail)
    Itemid=int(input("Enter ITEM ID: "))

def removeshoe(df, Itemid): 
    df.drop(Itemid, axis=0, inplace=True) 
    writeCSV(df)

def updateshoe (df, Itemid):
    Brand= input("Enter Brand: ")
    Category = input("Enter Category: ")
    Quantity = int(input("Enter Quantity: ")) 
    Price = int(input("Enter Price: "))
    df.loc[Itemid, : ] = [Brand, Category, Quantity, Price]
    writeCSV (df)

def showReportMenu(df):
    print("---Reports Menu---")
    print("Enter 1 to get total Cost of each itemid ") 
    print("Enter 2 to get total number of shoes in store")
    ch= int(input("Enter ur choice: "))
    if (ch == 1): reportTotalPrice(df)
    elif (ch == 2): reportTotalQuantity(df)
    
def reportTotalPrice(df): print("Total cost of each itemid is:- ", df['Price'] * df['Quantity'])
    
def reportTotalQuantity(df): print("Total Quantity is:- ",df['Quantity'].sum())
    

def showMainMenu(df):
    print() 
    print()
    print("-------Main Menu-------")
    print()
    print("Enter 1 to add new record ")
    print("Enter 2 to remove a record")
    print("Enter 3 to Update Shoe Details")
    print("Enter 4 to get shoe Detail")
    print("Enter 5 to print reports")
    print()
    print("---Data Visualisation---")
    print()
    print("Enter 6 to show Line Plot")
    print("Enter 7 to show Bar Plot")
    print()

    choice = int(input("Enter ur choice: "))

    if (choice == 1): addNewshoe(df)
    elif (choice == 2) : 
        Itemid= int(input("Enter ITEM ID: "))
        removeshoe(df, Itemid)
    elif (choice == 3) :
        Itemid= int(input("Enter ITEM ID: "))
        updateshoe(df, Itemid)
    elif (choice == 4) :
        Itemid = int(input("Enter ITEM ID: "))
        shoeDetail(df, Itemid)
    elif (choice == 5) : showReportMenu(df)
    elif(choice==6) : showLinePlot(df)
    elif(choice ==7) : showBarPlot(df)
    else : sys.exit()

