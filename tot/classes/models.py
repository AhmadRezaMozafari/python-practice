from dataclasses import dataclass

@dataclass
class Product:
    id:int
    name : str
    price : int
    stock : int


    def is_in_stock(self)->bool:
        return self.stock > 0

    def total_value(self)->int:
        return self.price * self.stock



@dataclass
class Order:
    id:int
    customer : str
    product : Product
    quantity : int
    unit_price: int
    def calculate_total(self) -> int:
        return self.unit_price * self.quantity

