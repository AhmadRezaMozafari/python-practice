def is_prime(n: int) -> bool:
    # اعداد کوچکتر از ۲ اول نیستند
    if n < 2:
        return False
    
    # عدد ۲ اول است
    if n == 2:
        return True
    
    # اعداد زوج بزرگتر از ۲ اول نیستند (بهینه‌سازی سریع)
    if n % 2 == 0:
        return False
    
    # فقط اعداد فرد را از ۳ تا ریشه‌ی دوم n بررسی می‌کنیم
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  # گام ۲ برای رد شدن از اعداد زوج
    
    return True

# تست
print(is_prime(7))   # خروجی: True
print(is_prime(10))  # خروجی: False
print(is_prime(2))   # خروجی: True
print(is_prime(1))   # خروجی: False


users = [
    {"name": "Ali", "age": 22, "active": True},
    {"name": "Reza", "age": 17, "active": False},
    {"name": "Sara", "age": 25, "active": True},
]

def getActiveUsers():
    result=[]
    for user in users:
        if user["active"] is True and user['age'] > 18:
            result.append(user)

    return result

getActiveUsers()

users = [
    {"name": "Ali", "age": 22, "active": True},
    {"name": "Reza", "age": 17, "active": False},
    {"name": "Sara", "age": 25, "active": True},
]

def getAverageActiveUsersAge():
    x=0
    y=0
    for user in users:
    
        if user["active"] is True:
            x+=user["age"]
            y+=1
        else:
            raise ZeroDivisionError('no active user!')

        
    return x/y

getAverageActiveUsersAge()

products = [
    {"name": "Laptop", "price": 800, "stock": 5},
    {"name": "Mouse", "price": 20, "stock": 0},
    {"name": "Keyboard", "price": 50, "stock": 10},
    {"name": "Monitor", "price": 300, "stock": 3},
]


def getExpensiveProduct():
    highPrice=[]
    for product in products:
        if product['stock'] > 0 :
            totalPrice=product["price"]*product["stock"]
            return highPrice




getExpensiveProduct()

numbers=[1,2,2,3,4,4,5,1,6,3]

numbers = list(dict.fromkeys(numbers))
print(numbers)



numbers=[12,5,34,2,87,1,56,19]

max=None
min=None

for x in numbers :
    if x is None or x > max:
        max = x
    if x is None or x < min:
        min = x

numbers = [12,-5,8,-2,0,17,-9,4,11,-6]


evenNumbers = 0
oddnumbers = 0
pnumbers=0
nnumbers=0

for x in numbers:
    if x > 0 :
        pnumbers+=1
        if x %2 ==0:
                evenNumbers+=1
        else :
            oddnumbers+=1
    else:
        nnumbers+=1

print(f'even {evenNumbers}\n odd {oddnumbers}\n P {pnumbers}\n N {nnumbers}')


numbers = [3,12,15,17,21,25,30,32,36,41]
newList=[]

for x in numbers :
    if x >= 10:
        if x % 3 == 0:
            newList.append(x)

print(newList)


numbers = [3,12,15,17,21,25,30,32,36,41]


for x in numbers :
    if x >= 10:
        if x % 3 != 0:
            numbers.remove(x)
    else:
        numbers.remove(x)
print(numbers)


students={'Ali':18,'Reza':12,'sara':19,'Mina':15,'Amir':9}

for student,score in students.items():
    if score >= 15:
        print(student)

average = sum(students.values()) / len(students)
print(average)

l = [1,3,2,1,4,3,1,5,2,6,3,3]

# for x in l:
#     c=dict.fromkeys(l,1)
#     for j in l:
#         if x == j:
#             c[x]+=1
freq = {}

for num in l:
    if num in freq:
        freq[num]+=1
    else :
        freq[num]=1

most_common=None
max_count = 0

for num,count in freq.items():
    if count > max_count:
        max_count = count
        most_common = num

data = {
    "name":"Ahmad",
    "city":"Tabriz",
    'age':26
}
rev = {}
for k,v in data.items():
    rev[v] = k

print(rev)


products = {
    "mouse": 800000,
    "keyboard": 1500000,
    "monitor": 7000000,
    "headset": 2000000
}

total_price=0
high_price = 0
more_than_m= []

for k,v in products.items():
    total_price += v
    if v > high_price:
        high_price=v
    if v > 1000000:
        more_than_m.append(v)

total_price = 0
high_price = 0
most_expensive = None
more_than_m = []

for k, v in products.items():
    total_price += v

    if v > high_price:
        high_price = v
        most_expensive = k

    if v > 1000000:
        more_than_m.append(k)

print("Total:", total_price)
print("Most expensive:", most_expensive, high_price)
print("Products over 1 million:", more_than_m)





def analyze_numbers(numbers:list) -> dict:
    result = {'even':0,'odd':0,'sum':0,'average':0,'max':0,'min':0}
    even=0
    odd= 0
    if len(numbers) != 0:
        def get_max(numbers:list)->int:
                Nmax= None 
                for number in numbers:
                    if Nmax is None or number > Nmax:
                     Nmax = number
                return Nmax

        def get_min(numbers:list)->int:
            Nmin= None 
            for number in numbers:
                if Nmin is None or number < Nmin:
                    Nmin = number
            return Nmin


        total = 0
        result['max'] = get_max(numbers)
        result['min'] = get_min(numbers)

        
        for number in numbers:
            total+=number
            if number %2 == 0:
                even +=1
                result['even']+=1
            else:
                odd +=1
                result['odd']+=1

        result['sum']=total

        result['average'] = total / len(numbers)
    else:
        raise ValueError('Empty list!')

    return result

def count_words(entery:str)->dict:
    sentence = entery.lower().split()
    freq={}

    for word in sentence:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1

    return freq



def filter_users(users:list[dict])->list[dict]:
    valid_users=[]
    for user in users:
        if user['age'] >=21 and user['active']:
            valid_users.append(user)

    return valid_users


def get_expensive_products(products:dict,min_price:int)->dict:
    result = {}

    for name in products:
        if products[name] > min_price:
            result[name] = products[name]

    return result


def find_duplicate_emails(emails:list)->list:
    result=[]
    freq={}

    for email in emails:
        if email in freq:
            freq[email]+=1
        else:
            freq[email]=1

    for em in freq:
        if freq[em] > 1:
            result.append(em)

    return result

def get_seles_report(orders:list[dict])->dict:
    total={}
    result = {}
    total_paid=0
    paid=0
    for order in orders:
        if order['status'] == 'paid':
            paid+=1
            total_paid+=order['amount']
        

            customer = order['customer']
            amount = order['amount']

            if customer in total:
                total[customer]+=amount
            else:
                total[customer]=amount
    top_customer=None
    max_amount=0

    for customer , amount in total.items():
        if amount > max_amount:
            max_amount = amount
            top_customer = customer
    
    result.update(
        {
            'total_paid':total_paid,
            'paid_count':paid,
            'customer_totals':total,
            'top_customer':top_customer,
        }
    )
    return result


def add_product(products:dict,name:str,price:int,stock:int)->int:
    # if not products:
    #     return 0
    # else:
    #     porduct_id=max(products)+1
    porduct_id=max(products,default=0)+1

    if price > 0 and stock >= 0:
        products.update({porduct_id:{
            'name':name,
            'price':price,
            'stock':stock
        }})
        return porduct_id

    return -1


products={
    1:{
        'name':'keyboard',
        'price':1500000,
        'stock':5
    },
    2:{
        'name':'mouse',
        'price':800000,
        'stock':10
    }
}
orders=[]

def register_order(products:dict,orders:list,customer:str,id:int,quantity:int):
    if id not in products:
        return 'Product dosent exist!'
    
    if quantity <= 0 :
        return 'مقدار درخواستی باید بزرگتر از 0 باشد.'

    product = products[id]

    if product['stock'] <= 0 :
        return 'این محصول تمام شده است.'

    if product['stock'] < quantity:
        return 'تعداد درخواستی شما بیشتر از تعداد محصولات است.'

    total_price = product['price'] * quantity

    order_id=len(orders)+1
    order= {'id':order_id,'customer':customer,'product_id':id,'total':total_price}
    
    product['stock'] -= quantity
    products[id] = product

    orders.append(order)
    
    return f"خرید انجام شد {product['stock']}"

orders = [
    {
        'id': 1,
        'customer': 'Ali',
        'product_id': 1,
        'quantity': 2,
        'total': 3000000
    },
    {
        'id': 2,
        'customer': 'Sara',
        'product_id': 2,
        'quantity': 3,
        'total': 2400000
    },
    {
        'id': 3,
        'customer': 'Ali',
        'product_id': 2,
        'quantity': 1,
        'total': 800000
    },
    {
        'id': 4,
        'customer': 'Reza',
        'product_id': 1,
        'quantity': 1,
        'total': 1500000
    },
    {
        'id': 5,
        'customer': 'Ali',
        'product_id': 1,
        'quantity': 1,
        'total': 1500000
    }
]



def calculate_customer_purchases(orders:list[dict], customer:str)->int:
    total=0
    for order in orders:
        if order['customer'] == customer:
            total += order['total']

    return total


def top_customer(orders):
    totals = {}

    for order in orders:
        customer = order['customer']
        amount = order['total']

        if customer in totals:
            totals[customer] += amount
        else:
            totals[customer] = amount

    if not totals:
        return None, 0

    top_name = None
    max_amount = 0

    for customer, amount in totals.items():
        if amount > max_amount:
            max_amount = amount
            top_name = customer

    return top_name, max_amount




import sqlite3

def init_db():
    with sqlite3.connect("sales.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price INTEGER NOT NULL CHECK(price > 0),
                stock INTEGER NOT NULL CHECK(stock >= 0)
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer TEXT NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL CHECK(quantity > 0),
                total INTEGER NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
        """)

init_db()


def add_product_db(name,price,stock):
    if not name or not name.strip():
        return {'success':False,"message":'name cannot be empty!'}
    if price <=0:
        return {'success':False,'message':'price most be higher than 0!'}
    if stock < 0 :
        return {'success':False,'message':'number of product must be gratter than 0 or 0!'}


    try:
        with sqlite3.connect('sales.db') as conn:
            cursor = conn.execute(
                "INSERT INTO products (name,price,stock) VALUES (?,?,?)",(name,price,stock)
            )
            new_id=cursor.lastrowid
            return {'success':True,'message':'product added','product_id':new_id}
    except sqlite3.Error as e:
        return {'success':False,'message':f'database Error {e}'}


# print(add_product_db("Keyboard", 1500000, 5))

def get_product_db():
    try:
        with sqlite3.connect('sales.db') as conn:
            row = conn.execute("SELECT * FROM products").fetchall()
            print(row)
    finally:
        conn.close()

def get_product_by_id(product_id):
    try:
        with sqlite3.connect('sales.db') as conn:
            row = conn.execute('SELECT * FROM products WHERE id = ?',(product_id,)).fetchone()
            return row
    finally:
        conn.close()



def update_product_stock(product_id: int, new_stock: int) -> dict:
    if new_stock < 0:
        return {
            'success': False,
            'message': 'Stock cannot be negative!'
        }

    conn = sqlite3.connect('sales.db')

    try:
        with conn:
            cursor = conn.execute(
                'UPDATE products SET stock = ? WHERE id = ?',
                (new_stock, product_id)
            )

            if cursor.rowcount == 0:
                return {
                    'success': False,
                    'message': 'Product not found!'
                }

        return {
            'success': True,
            'message': 'Stock updated successfully!'    
        }

    except sqlite3.Error as e:
        return {
            'success': False,
            'message': f'Database error: {e}'
        }

    finally:
        conn.close()



def delete_product(product_id):
    conn = sqlite3.connect('sales.db')

    try:
        with conn:
            cursor = conn.execute('DELETE FROM products WHERE id = ?',(product_id,))
        if cursor.rowcount == 0:
            return{
                'success':False,
                'message':'product dont exist'
            }
        return {
            'success':True,
            'message':'product has been deleted'
        }
    finally:
        conn.close()