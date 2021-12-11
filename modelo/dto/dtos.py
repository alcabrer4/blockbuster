from datetime import date

class Video_StoresDTO:
    def __init__(self, code:int, address:str, phone:int, email:str) -> None:
        self.code = code
        self.address = address
        self.phone = phone
        self.email = email
    
    def get_code(self):
        return self.code
    def set_code(self,x:int):
        self.code = x
        
    def get_address(self):
        return self.address
    def set_address(self, x:str):
        self.address = x

    def get_phone(self):
        return self.phone
    def set_phone(self,x:int):
        self.phone = x
    
    def get_email(self):
        return self.email
    def set_email(self,x:str):
        self.email = x


class Format_TypesDTO:
    def __init__(self, code:int, description:str) -> None:
        self.code = code
        self.description = description
    
    def get_code(self):
        return self.code
    def set_code(self,x:int):
        self.code = x
    
    def get_description(self):
        return self.description
    def set_description(self,x:str):
        self.description = x


class Genres_CodesDTO:
    def __init__(self, code:int, description:str) -> None:
        self.code = code
        self.description = description
    
    def get_code(self):
        return self.code
    def set_code(self,x:int):
        self.code = x
    
    def get_description(self):
        return self.description
    def set_description(self,x:str):
        self.description = x


class MoviesDTO:
    def __init__(self, code:int, formatid:int, genreid:int, storeid:int, release:date, title:str, stock:int, rntlrate:float, price:float) -> None:
        self.code = code
        self.formatid = formatid
        self.genreid = genreid
        self.storeid = storeid
        self.release = release
        self.title = title
        self.stock = stock
        self.rntlrate = rntlrate
        self.price = price
    
    def get_code(self):
        return self.code
    def set_code(self,x:int):
        self.code = x
    
    def get_formatid(self):
        return self.formatid
    def set_formatid(self,x:int):
        self.formatid = x
    
    def get_genreid(self):
        return self.genreid
    def set_genreid(self,x:int):
        self.genreid = x

    def get_storeid(self):
        return self.storeid
    def set_storeid(self,x:int):
        self.storeid = x

    def get_release(self):
        return self.release
    def set_release(self,x:date):
        self.release = x
    
    def get_title(self):
        return self.title
    def set_title(self,x:str):
        self.title = x

    def get_stock(self):
        return self.stock
    def set_stock(self,x:int):
        self.stock = x

    def get_rntlrate(self):
        return self.rntlrate
    def set_rntlrate(self,x:float):
        self.rntlrate = x

    def get_price(self):
        return self.price
    def set_price(self,x:float):
        self.price = x


class ActorsDTO:
    def __init__(self, code:int, firstname:str, lastname:str, gender:str) -> None:
        self.code = code
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
    
    def get_code(self):
        return self.code
    def set_code(self,x:int):
        self.code = x
    
    def get_firstname(self):
        return self.firstname
    def set_firstname(self,x:str):
        self.firstname = x
    
    def get_lastname(self):
        return self.lastname
    def set_lastname(self,x:str):
        self.lastname = x
    
    def get_gender(self):
        return self.gender
    def set_gender(self,x:str):
        self.gender = x


class Movie_CastDTO:
    def __init__(self, code:int, movieid:int, actorid:int) -> None:
        self.code = code
        self.movieid = movieid
        self.actorid = actorid

    def get_code(self):
        return self.code
    def set_code(self,x:int):
        self.code = x
    
    def get_movieid(self):
        return self.movieid
    def set_movieid(self,x:int):
        self.movieid = x
    
    def get_actorid(self):
        return self.actorid
    def set_actorid(self,x:int):
        self.actorid = x


class Rental_Status_CodesDTO:
    def __init__(self, code:int,description:str) -> None:
        self.code = code
        self.description = description
    
    def get_code(self):
        return self.code
    def set_code(self,x:int):
        self.code = x

    def get_description(self):
        return self.description 
    def set_description(self,x:str):
        self.description = x


class CostumersDTO:
    def __init__(self, code:int, firstname:str, lastname:str, phone:int, email:str, address:str) -> None:
        self.code = code
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.address = address

    def get_code(self):
        return self.code
    def set_code(self,x:int):
        self.code = x
    
    def get_firstname(self):
        return self.firstname
    def set_firstname(self,x:str):
        self.firstname = x
    
    def get_lastname(self):
        return self.lastname
    def set_lastname(self,x:str):
        self.lastname = x

    def get_phone(self):
        return self.phone
    def set_phone(self,x:int):
        self.phone = x
    
    def get_email(self):
        return self.email
    def set_email(self,x:str):
        self.email = x
    
    def get_address(self):
        return self.address
    def set_address(self,x:str):
        self.address = x


class Costumer_RentalsDTO:
    def __init__(self, code:int, costumerid:int, movieid:int, rntlstatusid:int, rntlout:date, rntlreturned:date, amountdue:float) -> None:
        self.code = code
        self.costumerid = costumerid
        self.movieid = movieid
        self.rntlstatusid = rntlstatusid
        self.rntlout = rntlout
        self.rntlreturned =rntlreturned
        self.amountdue = amountdue

    def get_code(self):
        return self.code
    def set_code(self,x:int):
        self.code = x

    def get_costumerid(self):
        return self.costumerid
    def set_costumerid(self,x:int):
        self.costumerid = x

    def get_movieid(self):
        return self.movieid
    def set_movieid(self,x:int):
        self.movieid = x

    def get_rntlstatusid(self):
        return self.rntlstatusid
    def set_rntlstatusid(self,x:int):
        self.rntlstatusid = x

    def get_rntlout(self):
        return self.rntlout
    def set_rntlout(self,x:date):
        self.rntlout = x

    def get_rntlreturned(self):
        return self.rntlreturned
    def set_rntlreturned(self,x:date):
        self.rntlreturned = x

    def get_amountdue(self):
        return self.amountdue
    def set_amountdue(self,x:float):
        self.amountdue = x


class Payment_MethodsDTO:
    def __init__(self, code:int, description:str) -> None:
        self.code = code
        self.description = description

    def get_code(self):
        return self.code
    def set_code(self,x:int):
        self.code = x
    
    def get_description(self):
        return self.description
    def set_description(self,x:str):
        self.description = x


class AccountsDTO:
    def __init__(self, code:int, costumerid:int, paymethodid:int, accountname:str) -> None:
        self.code = code
        self.costumerid = costumerid
        self.paymethodid = paymethodid
        self.accountname = accountname
    
    def get_code(self):
        return self.code
    def set_code(self,x:int):
        self.code = x

    def get_costumerid(self):
        return self.costumerid
    def set_costumerid(self,x:int):
        self.costumerid = x

    def get_paymethodid(self):
        return self.paymethodid
    def set_paymethod(self,x:int):
        self.paymethodid = x

    def get_accountname(self):
        return self.accountname
    def set_accountname(self,x:str):
        self.accountname = x


class Transaction_TypesDTO:
    def __init__(self, code:int, description:str) -> None:
        self.code = code
        self.description = description

    def get_code(self):
        return self.code
    def set_code(self,x:int):
        self.code = x

    def get_description(self):
        return self.description
    def set_description(self,x:str):
        self.description = x


class Financial_TransactionsDTO:
    def __init__(self, code:int, accountid:int, itemrntlid:int, trantypeid:int, trandate:date, tranammount:date) -> None:
        self.code = code
        self.accountid = accountid
        self.itemrntlid = itemrntlid
        self.trantypeid = trantypeid
        self.trandate = trandate
        self.tranammount = tranammount
    
    def get_code(self):
        return self.code
    def set_code(self,x:int):
        self.code = x
    
    def get_accountid(self):
        return self.accountid
    def set_accountid(self,x:int):
        self.accountid = x
    
    def get_itemrntlid(self):
        return self.itemrntlid
    def set_itemrntlid(self,x:int):
        self.itemrntlid = x

    def get_trantypeid(self):
        return self.trantypeid
    def set_trantypeid(self,x:int):
        self.trantypeid = x

    def get_trandate(self):
        return self.trandate
    def set_trandate(self,x:date):
        self.trandate = x
    
    def get_tranammount(self):
        return self.tranammount
    def set_tranammount(self,x:date):
        self.tranammount = x