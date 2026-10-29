from pydantic import BaseModel,Field


class ProductCreate(BaseModel):
    name:str = Field(...,min_length=2,description='product name:')
    price:int = Field(...,gt=0,description='price most be gratter than 0!')
    stock:int = Field(...,ge=0,description='stock most be 0 or bigger!')


class ProductResponse(BaseModel):
    id: int
    name:str
    price:int
    stock:int

class StockUpdate(BaseModel):
    new_stock:int =Field(...,ge=0)
    