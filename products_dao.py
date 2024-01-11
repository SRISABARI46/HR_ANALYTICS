from sql_connector import get_sql_connection

def get_all_products(connection):


    cursor = connection.cursor()
    query=("SELECT products_list.product_id,products_list.product_name,products_list.uom_id,products_list.price_per_unit,uom.uom_name FROM products_list inner join uom on products_list.uom_id=uom.uom_id")
    cursor.execute(query)
    response=[]
    for (product_id,product_name,uom_id,uom_name,price_per_unit) in cursor:
        response.append(
            {
                'product_id':product_id,
                'product_name':product_name,
                'uom_id':uom_id,
                'uom_name':uom_name,
                'price_per_unit':price_per_unit
            }
        )
        #print(product_id,product_name,uom ,uom_name,price_per_unit)

    return response

def insert_new_product(connection, products_list):
    cursor = connection.cursor()
    query = ("INSERT INTO products_list "
             "(product_name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (products_list['product_name'], products_list['uom_id'], products_list['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products_list where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__=="__main__":
    connection=get_sql_connection()
    #print(get_all_products(connection))
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': '2',
        'price_per_unit': 20
    }))



