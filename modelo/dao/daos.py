from modelo import conexion
from modelo.dto import dtos as do
import abc

class DAO:
    def __init__(self, table, cnx) -> None:
        self.table = table
        self.cnx = cnx
    
    def get_cursor(self):
        cursor = self.cnx.cursor()
        query = "SELECT * FROM " + self.table + ";"
        cursor.execute(query)
        return cursor

    @abc.abstractmethod
    def get_data(self):
        pass

    @abc.abstractmethod
    def insert_data(self):
        pass

    @abc.abstractmethod
    def update_data(self):
        pass

    @abc.abstractmethod
    def delete_data(self):
        pass


class Video_StoresDAO(DAO):
    def __init__(self, cnx) -> None:
        super().__init__("Video_Stores", cnx)

    def get_data(self):
        cursor = self.get_cursor()
        stores = []
        for (code, address, phone, email) in cursor:
            dt = do.Video_StoresDTO(code, address, phone, email)
            stores.append(dt)
        return stores
    
    def insert_data(self, dto:do.Video_StoresDTO):
        cursor = self.cnx.cursor()
        putin = "INSERT INTO " + self.table + " (store_adress, store_phone, store_email) VALUES (%s, %s, %s)"
        values = (dto.address , dto.phone, dto.email)
        cursor.execute(putin,values)
        conexion.cnx.commit()

    def update_data(self, dto:do.Video_StoresDTO):
        cursor = self.cnx.cursor()
        update1 = "UPDATE " + self.table + " SET store_address = '%s' WHERE store_address = '%s'"
        value1 = (dto.address, dto.address)
        cursor.execute(update1,value1)
        update2 = "UPDATE " + self.table + " SET store_phone = '%s' WHERE store_phone = '%s'"
        value2 = (dto.phone, dto.phone)
        cursor.execute(update2,value2)
        update3 = "UPDATE " + self.table + " SET store_email = '%s' WHERE store_email = '%s'"
        value3 = (dto.email, dto.email)
        cursor.execute(update3,value3)
        conexion.cnx.commit()

    def delete_data(self):
        return super().delete_data()


class Format_TypesDAO(DAO):
    def __init__(self,cnx) -> None:
        super().__init__("Format_Types", cnx)

    def get_data(self) -> list:
        cursor = self.get_cursor()
        descriptions = []
        for (code, description) in cursor:
            dt = do.Format_TypesDTO(code, description)
            descriptions.append(dt)
        return descriptions

    def insert_data(self, dto:do.Format_TypesDTO):
        cursor = self.cnx.cursor()
        putin = "INSERT INTO " + self.table + " (format_type_description) VALUES (%s)"
        values = (dto.description)
        cursor.execute(putin,values)
        conexion.cnx.commit()

    def update_data(self, dto:do.Format_TypesDTO):
        cursor = self.cnx.cursor()
        update = "UPDATE " + self.table + " SET format_type_description = '%s' WHERE format_type_description = '%s'"
        value = (dto.description, dto.description)
        cursor.execute(update,value)
        conexion.cnx.commit()


class Genre_CodesDAO(DAO):
    def __init__(self,cnx) -> None:
        super().__init__("Genre_Codes", cnx)

    def get_data(self) -> list:
        cursor = self.get_cursor()
        descriptions = []
        for (code, description) in cursor:
            dt = do.Genres_CodesDTO(code, description)
            descriptions.append(dt)
        return descriptions
    
    def insert_data(self, dto:do.Genres_CodesDTO):
        cursor = self.cnx.cursor()
        putin = "INSERT INTO " + self.table + " (genre_description) VALUES (%s)"
        values = (dto.description)
        cursor.execute(putin,values)
        conexion.cnx.commit()
    
    def update_data(self, dto:do.Genres_CodesDTO):
        cursor = self.cnx.cursor()
        update1 = "UPDATE " + self.table + " SET genre_description = '%s' WHERE genre_description = '%s'"
        value1 = (dto.description, dto.description)
        cursor.execute(update1,value1)
        conexion.cnx.commit()


class MoviesDAO(DAO):
    def __init__(self,cnx) -> None:
        super().__init__("Movies", cnx)

    def get_data(self) -> list:
        cursor = self.get_cursor()
        movies = []
        for (code, formatid, genreid, storeid, release, title, stock, rntlrate, price) in cursor:
            dt = do.MoviesDTO(code, formatid, genreid, storeid, release, title, stock, rntlrate, price)
            movies.append(dt)
        return movies

    def insert_data(self, dto:do.MoviesDTO):
        cursor = self.cnx.cursor()
        putin = "INSERT INTO " + self.table + " (format_type_code, genre_code, store_id, release_year, movie_title, number_in_stock, rental_daily_rate, sale_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (dto.formatid, dto.genreid, dto.storeid, dto.release, dto.title, dto.stock, dto.rntlrate, dto.price)
        cursor.execute(putin,values)
        conexion.cnx.commit()

    def update_data(self, dto:do.MoviesDTO):
        cursor = self.cnx.cursor()
        update1 = "UPDATE " + self.table + " SET format_type_code = '%s' WHERE format_type_code = '%s'"
        value1 = (dto.formatid, dto.formatid)
        cursor.execute(update1,value1)
        update2 = "UPDATE " + self.table + " SET genre_code = '%s' WHERE genre_code = '%s'"
        value2 = (dto.genreid, dto.genreid)
        cursor.execute(update2,value2)
        update3 = "UPDATE " + self.table + " SET store_id = '%s' WHERE store_id = '%s'"
        value3 = (dto.storeid, dto.storeid)
        cursor.execute(update3,value3)
        update4 = "UPDATE " + self.table + " SET release_year = '%s' WHERE release_year = '%s'"
        value4 = (dto.release, dto.release)
        cursor.execute(update4,value4)
        update5 = "UPDATE " + self.table + " SET movie_title = '%s' WHERE movie_title = '%s'"
        value5 = (dto.title, dto.title)
        cursor.execute(update5,value5)
        update6 = "UPDATE " + self.table + " SET number_in_stock = '%s' WHERE number_in_stock = '%s'"
        value6 = (dto.stock, dto.stock)
        cursor.execute(update6,value6)
        update7 = "UPDATE " + self.table + " SET rental_daily_rate = '%s' WHERE rental_daily_rate = '%s'"
        value7 = (dto.rntlrate, dto.rntlrate)
        cursor.execute(update7,value7)
        update8 = "UPDATE " + self.table + " SET sale_price = '%s' WHERE sale_price = '%s'"
        value8 = (dto.price, dto.price)
        cursor.execute(update8,value8)
        conexion.cnx.commit()


class ActorsDAO(DAO):
    def __init__(self,cnx) -> None:
        super().__init__("Actors", cnx)

    def get_data(self) -> list:
        cursor = self.get_cursor()
        actors = []
        for (code, firstname, lastname, gender) in cursor:
            dt = do.ActorsDTO(code, firstname, lastname, gender)
            actors.append(dt)
        return actors

    def insert_data(self, dto:do.ActorsDTO):
        cursor = self.cnx.cursor()
        putin = "INSERT INTO " + self.table + " (actor_first_name, actor_last_name, actor_gender) VALUES (%s, %s, %s)"
        values = (dto.firstname, dto.lastname, dto.gender)
        cursor.execute(putin,values)
        conexion.cnx.commit()

    def update_data(self, dto:do.ActorsDTO):
        cursor = self.cnx.cursor()
        update1 = "UPDATE " + self.table + " SET actor_first_name = '%s' WHERE actor_first_name = '%s'"
        value1 = (dto.firstname, dto.firstname)
        cursor.execute(update1,value1)
        update2 = "UPDATE " + self.table + " SET actor_last_name = '%s' WHERE actor_last_name = '%s'"
        value2 = (dto.lastname, dto.lastname)
        cursor.execute(update2,value2)
        update3 = "UPDATE " + self.table + " SET actor_gender = '%s' WHERE actor_gender = '%s'"
        value3 = (dto.gender, dto.gender)
        cursor.execute(update3,value3)
        conexion.cnx.commit()


class Movie_CastDAO(DAO):
    def __init__(self,cnx) -> None:
        super().__init__("Movie_Cast", cnx)

    def get_data(self) -> list:
        cursor = self.get_cursor()
        l = []
        for (code, movieid, actorid) in cursor:
            dt = do.Movie_CastDTO(code, movieid, actorid)
            l.append(dt)
        return l
    
    def insert_data(self, dto:do.Movie_CastDTO):
        cursor = self.cnx.cursor()
        putin = "INSERT INTO " + self.table + " (movie_id, actor_id) VALUES (%s, %s)"
        values = (dto.movieid, dto.actorid)
        cursor.execute(putin,values)
        conexion.cnx.commit()
    
    def update_data(self, dto:do.Movie_CastDTO):
        cursor = self.cnx.cursor()
        update1 = "UPDATE " + self.table + " SET movie_id = '%s' WHERE movie_id = '%s'"
        value1 = (dto.movieid, dto.movieid)
        cursor.execute(update1,value1)
        update2 = "UPDATE " + self.table + " SET actor_id = '%s' WHERE actor_id = '%s'"
        value2 = (dto.actorid, dto.actorid)
        cursor.execute(update2,value2)
        conexion.cnx.commit()


class Rental_Status_CodesDAO(DAO):
    def __init__(self,cnx) -> None:
        super().__init__("Rental_Status_Codes", cnx)

    def get_data(self) -> list:
        cursor = self.get_cursor()
        descriptions = []
        for (code, description) in cursor:
            dt = do.Rental_Status_CodesDTO(code, description)
            descriptions.append(dt)
        return descriptions
    
    def insert_data(self, dto:do.Rental_Status_CodesDTO):
        cursor = self.cnx.cursor()
        putin = "INSERT INTO " + self.table + " (rental_status_description) VALUES (%s)"
        values = (dto.description)
        cursor.execute(putin,values)
        conexion.cnx.commit()


class CostumersDAO(DAO):
    def __init__(self,cnx) -> None:
        super().__init__("Costumers", cnx)

    def get_data(self) -> list:
        cursor = self.get_cursor()
        costumers = []
        for (code, firstname, lastname, phone, email, address) in cursor:
            dt = do.CostumersDTO(code, firstname, lastname, phone, email, address)
            costumers.append(dt)
        return costumers

    def insert_data(self, dto:do.CostumersDTO):
        cursor = self.cnx.cursor()
        putin = "INSERT INTO " + self.table + " (costumer_first_name, costumer_last_name, costumer_phone, costumer_email, costumer_address) VALUES (%s, %s, %s, %s, %s)"
        values = (dto.firstname, dto.lastname, dto.phone, dto.email, dto.address)
        cursor.execute(putin,values)
        conexion.cnx.commit()


class Costumer_RentalsDAO(DAO):
    def __init__(self,cnx) -> None:
        super().__init__("Costumer_Rentals", cnx)

    def get_data(self) -> list:
        cursor = self.get_cursor()
        cr = []
        for (code, costumerid, movieid, rntlstatusid, rntlout, rntlreturned, amountdue) in cursor:
            dt = do.Costumer_RentalsDTO(code, costumerid, movieid, rntlstatusid, rntlout, rntlreturned, amountdue)
            cr.append(dt)
        return cr

    def insert_data(self, dto:do.Costumer_RentalsDTO):
        cursor = self.cnx.cursor()
        putin = "INSERT INTO " + self.table + " (costumer_id, movie_id, rental_status_code, rental_date_out, rental_date_returned, rental_amount_due) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (dto.costumerid, dto.movieid, dto.rntlstatusid, dto.rntlout, dto.rntlreturned, dto.amountdue)
        cursor.execute(putin,values)
        conexion.cnx.commit()


class Payment_MethodsDAO(DAO):
    def __init__(self,cnx) -> None:
        super().__init__("Payment_Methods", cnx)

    def get_data(self) -> list:
        cursor = self.get_cursor()
        descriptions = []
        for (code, description) in cursor:
            dt = do.Payment_MethodsDTO(code, description)
            descriptions.append(dt)
        return descriptions
    
    def insert_data(self, dto:do.Payment_MethodsDTO):
        cursor = self.cnx.cursor()
        putin = "INSERT INTO " + self.table + " (payment_method_description) VALUES (%s)"
        values = (dto.description)
        cursor.execute(putin,values)
        conexion.cnx.commit()


class AccountsDAO(DAO):
    def __init__(self,cnx) -> None:
        super().__init__("Accounts", cnx)

    def get_data(self) -> list:
        cursor = self.get_cursor()
        accounts = []
        for (code, costumerid, paymethodid, accountname) in cursor:
            dt = do.AccountsDTO(code, costumerid, paymethodid, accountname)
            accounts.append(dt)
        return accounts

    def insert_data(self, dto:do.AccountsDTO):
        cursor = self.cnx.cursor()
        putin = "INSERT INTO " + self.table + " (costumer_id, payment_method_code, account_name) VALUES (%s, %s, %s)"
        values = (dto.costumerid, dto.paymethodid, dto.accountname)
        cursor.execute(putin,values)
        conexion.cnx.commit()


class Transaction_TypesDAO(DAO):
    def __init__(self,cnx) -> None:
        super().__init__("Transaction_Types", cnx)

    def get_data(self) -> list:
        cursor = self.get_cursor()
        descriptions = []
        for (code, description) in cursor:
            dt = do.Transaction_TypesDTO(code, description)
            descriptions.append(dt)
        return descriptions

    def insert_data(self, dto:do.Transaction_TypesDTO):
        cursor = self.cnx.cursor()
        putin = "INSERT INTO " + self.table + " (transaction_type_description) VALUES (%s)"
        values = (dto.description)
        cursor.execute(putin,values)
        conexion.cnx.commit()


class Financial_TransactionsDAO(DAO):
    def __init__(self,cnx) -> None:
        super().__init__("Financial_Transactions", cnx)

    def get_data(self) -> list:
        cursor = self.get_cursor()
        ft = []
        for (code, accountid, itemrntlid, trantypeid, trandate, tranammount) in cursor:
            dt = do.Financial_TransactionsDTO(code, accountid, itemrntlid, trantypeid, trandate, tranammount)
            ft.append(dt)
        return ft

    def insert_data(self, dto:do.Financial_TransactionsDTO):
        cursor = self.cnx.cursor()
        putin = "INSERT INTO " + self.table + " (account_id, item_rental_id, transaction_type_code, transaction_date, transaction_amount) VALUES (%s, %s, %s, %s, %s)"
        values = (dto.accountid, dto.itemrntlid, dto.trantypeid, dto.trandate, dto.tranammount)
        cursor.execute(putin,values)
        conexion.cnx.commit()