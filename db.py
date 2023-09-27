import psycopg2


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            database='json_15_00',
            password='123456',
            host='localhost',
            user='postgres'
        )

    def manager(self, sql, *args,
                commit=False,
                fetchone=False,
                fetchall=False):
        with self.connection as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                if fetchone:
                    result = db.fetchone()
                if fetchall:
                    result = db.fetchall()
                return result


class TableCreator(Database):
    def create_categories_table(self):
        sql = """
        DROP TABLE IF EXISTS categories;
        CREATE TABLE IF NOT EXISTS categories(
            category_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            category_name VARCHAR(100)
        );
        """
        self.manager(sql, commit=True)


    def create_products_table(self):
        sql = """
            DROP TABLE IF EXISTS products;
            CREATE TABLE IF NOT EXISTS products(
            products_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            title VARCHAR(200),
            description TEXT,
            price Float,
            image text,
            rate Float,
            rate_count INTEGER,
            category_id INTEGER references categories(category_id)
            );
        """
        self.manager(sql, commit=True)


class Manager(Database):
    def insert_categories(self, categories_list):
        sql = "Insert into categories(category_name) values (%s);"
        for category in categories_list:
            self.manager(sql, category, commit=True)
            print(f'Added category {category}')



# creator = TableCreator()
# creator.create_categories_table()
# creator.create_products_table()
