import qrcode
from colorama import Fore,init
init(autoreset=True)
PRODUCTS= []

def read_from_database():
    f=open("database.txt", "r")
    for line in f:
       result=line.split(',')
       my_dict={'code':result[0], 'name':result[1], 'price':result[2], 'count':result[3]}
       PRODUCTS.append(my_dict)
    f.close()
read_from_database()

def write_to_database():
    f=open("database.txt", "w")
    for product in PRODUCTS:
            code=product['code']
            name=product['name']
            price=product['price']
            count=product['count']
    f.write(code + "," +name + ","+price+ ","+count)
    f.close()


def show_menue():
    print("1_ Add")
    print("2_ Edit")
    print("3_ Remove")
    print("4_ Search")
    print("5_ Show List")
    print("6_ Buy")
    print("7_ Save & Exit")
    print("8_ product To QrCode")

def add():
    code=input("enter code : ")
    name=input("enter name : ")
    price=input("enter price : ")
    count=input("enter count : ")
    new_product={'code':code, 'name':name, 'price':price, 'count':count}
    PRODUCTS.append(new_product)
def edit():
    user_input=input("Enter Your Code Product: ")
    for product in PRODUCTS:
        if user_input==product['code']: 
            print(Fore.RED+"-----------------------------------------")
            print(f"{' Name':5}", f"{' Price':8}", f"{' Count':10}")
            print(f"{product['name']:5}", f"{product['price']:8}", f"{product['count']:10}")
            print(Fore.RED+"-----------------------------------------")
            print(Fore.BLUE+"1_""Name""\n""2_""Price""\n""3_""Count")

            field_number=int(input("Jahat Virayesh Field Mored Nazar RA Vared Konid :"))
            if field_number==1:
                    new_name=input("Enter New Name :")
                    product['name']=new_name
                    print(Fore.GREEN+"Name Mahsool Mored Nazar Virayesh Gardid") 
                    break
            if field_number==2:
                    new_price=input("Enter New Price :")
                    product['price']=new_price
                    print(Fore.GREEN+"Gheymat Mahsool Mored Nazar Virayesh Gardid") 
                    break
            if field_number==3:
                    new_count=input("Enter New Count :")
                    product['count']=new_count
                    print(Fore.GREEN+"Count Mahsool Mored Nazar Virayesh Gardid") 
                    break  
    else:
        print(Fore.RED+" ** (( Not Found  )) ** ")    
def remove():
    user_input=input("Enter Your Code : ")
    for product in PRODUCTS.copy():
        if user_input==product.get('code'): 
            PRODUCTS.remove(product)
            print(Fore.RED+"Mahsool Mored Nazar Hazf Gardid") 
            show_list()
            break
    else:
          print("code ra eshtebah vared kardid")   

def search():
    user_input=input("Enter Your Keyword : ")
    for product in PRODUCTS:
        if user_input==product['code'] or user_input==product['name']: 
            print(f"{product['code']:5}", f"{product['name']:8}", f"{product['price']:10}")
            break
    else:
        print(" ** (( Not Found  )) ** ")    

def show_list():
    print(f"{'code':5}", f"{'Name':8}", f"{'Price':10}")
    for product in PRODUCTS:
        print(f"{product['code']:5}", f"{product['name']:8}", f"{product['price']:10}")
def buy():
   global basket
   basket=[]
   
   while True:
    user_input=int(input("Enter Code Product : "))                   
    for product in PRODUCTS:
                    if user_input==int(product['code']) : 
                        input_user_product_count=int(input("Tedad mahsool jahat kharid ra nared namayid : "))
                        if input_user_product_count>int(product['count']):
                            print("mahsool mored nazar dar anbar mojod nist !")
                        else:
                            int_product_count=int(product['count'])
                            int_baghimande_anbar=int_product_count-input_user_product_count
                            product['count']=str(int_baghimande_anbar)
                            basket=product
                            print(basket)
                        break
    else:
                print(" ** (( Mahsool Mored nazar yaft nashod  )) ** ")    


def product_qrcode():
    user_input=input("Enter Code Product : ")
    for product in PRODUCTS:
        if user_input==product['code'] : 
          code=product['code']
          name=product['name']
          price=product['price']
          count=product['price']
          img=qrcode.make(code+" | "+name+" | "+price+" | "+count)
          img.save("Product_details.jpg")
          print("QrCode masool mored nazar sakhteh shod .")
          break
    else:
        print(" ** (( Not Found  )) ** ")    
     

print("WellCome To My Store ")    
print("Loading . . . ")    
print("Data Loaded ")   

while True:
    show_menue()
    choice=int(input("Enter Your Choice : "))

    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
      remove()
    elif choice==4:
        search()
    elif choice==5:
      show_list()
    elif choice==6:
        buy()
    elif choice==7:
        write_to_database()
        exit(0)
    elif choice==8:
        product_qrcode()    
    else:
        print("dorost enkhab konid !!!")    




