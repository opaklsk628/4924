import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Benefit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                  Column('id', Integer, primary_key=True),
                                  Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                  Column('employee_id', Integer, ForeignKey('employee.id'))
)


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name

class Products(Model):
    __tablename__ = 'Products'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    price = Column(Integer, nullable=False)
    status = Column(String(3), nullable=False)
    created_at = Column(Integer, nullable=False)
    categorie_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    supplier_id = Column(Integer, nullable=False)
    branch_id = Column(Integer, nullable=False)
    brand_id = Column(Integer, nullable=False)

class Orders(Model):
    __tablename__ = 'Orders'
    orders_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    status = Column(String(3), nullable=False)
    created_at = Column(Integer, nullable=False)

class Order_items(Model):
    __tablename__ = 'Order_items'
    orders_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

class Supplier(Model):
    __tablename__ = 'Supplier'
    Supplier_id = Column(Integer, primary_key=True)
    supplier_name = Column(String(150), nullable=False)
    created_at = Column(Integer, nullable=False)

class Invoices(Model):
    __tablename__ = 'Invoices'
    invoices_number = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    invoices_date = Column(Date, default=datetime.date.today(), nullable=True)
    invoices_details = Column(String(250), nullable=False)
    payments_id = Column(Integer, nullable=False)
    delivery_id = Column(Integer, nullable=False)

class Payments(Model):
    __tablename__ = 'Payments'
    payments_id = Column(Integer, primary_key=True)
    invoices_number = Column(Integer, nullable=False)
    Payment_date = Column(Date, default=datetime.date.today(), nullable=True)
    payment_amount = Column(Integer, nullable=False)

class Delivery_address(Model):
    __tablename__ = 'Delivery_address'
    delivery_id = Column(Integer, primary_key=True)
    foremane = Column(String(150), nullable=False)
    address = Column(String(200), nullable=False)
    postcode = Column(Integer, nullable=False)
    phone_number = Column(Integer, nullable=False)
    email = Column(String(100), nullable=False)

class Categories(Model):
    __tablename__ = 'Categories'
    categorie_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)

class Branch(Model):
    __tablename__ = 'Branch'
    branch_id = Column(Integer, primary_key=True)
    address = Column(String(200), nullable=False)
    phone_number = Column(Integer, nullable=False)

class Staff(Model):
    __tablename__ = 'Staff'
    Staff_id = Column(Integer, primary_key=True)
    staff_name = Column(String(50), nullable=False)
    phone_number = Column(Integer, nullable=False)

class Brands(Model):
    __tablename__ = 'Brands'
    brand_id = Column(Integer, primary_key=True)
    brand_name = Column(String(50), nullable=False)
    brand_info = Column(String(100), nullable=False)