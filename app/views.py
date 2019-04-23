from flask_appbuilder import ModelView, has_access
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, Products, Orders, Order_items, Supplier, Invoices, Payments, Delivery_address, Categories, Branch, Brands
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView



def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class ProductsView(ModelView):
    datamodel = SQLAInterface(Products)
    list_columns = ['id', 'name', 'price', 'status', 'created_at', 'categorie_id', 'quantity', 'supplier_id', 'branch_id', 'brand_id']

class BrandsView(ModelView):
    datamodel = SQLAInterface(Brands)
    list_columns = ['brand_id','brand_name', 'brand_info']

class OrdersView(ModelView):
    datamodel = SQLAInterface(Orders)
    list_columns = ['orders_id', 'user_id', 'status', 'created_at']

class OrderitemsView(ModelView):
    datamodel = SQLAInterface(Order_items)
    list_columns = ['order_id', 'product_id', 'quantity']

class SupplierView(ModelView):
    datamodel = SQLAInterface(Supplier)
    list_columns = ['Supplier_id', 'supplier_name', 'created_at']

class InvoicesView(ModelView):
    datamodel = SQLAInterface(Invoices)
    list_columns = ['invoices_number', 'order_id', 'invoices_date']

class PaymentsView(ModelView):
    datamodel = SQLAInterface(Payments)
    list_columns = ['payments_id', 'invoices_number', 'Payment_date', 'payment_amount']

class Delivery_addressView(ModelView):
    datamodel = SQLAInterface(Delivery_address)
    list_columns = ['delivery_id', 'foremane', 'address', 'postcode', 'phone_number', 'email']

class CategoriesView(ModelView):
    datamodel = SQLAInterface(Categories)
    list_columns = ['categorie_id', 'name', 'description']

class BranchView(ModelView):
    datamodel = SQLAInterface(Branch)
    list_columns = ['branch_id', 'address', 'phone_number']

class ProductPageView(BaseView):
    default_view = 'hit_product'

    @expose('/hit_product/')
    def hit_product(self):
        param1 = '2019 Hit Product'
        self.update_redirect()
        return self.render_template('product.html', param1=param1)

    @expose('/phone/')
    def phone(self):
        param1 = 'Phone'
        self.update_redirect()
        return self.render_template('product.html', param1=param1)

class PaymentPageView(BaseView):
    default_view = 'payment'

    @expose('/payment/')
    def payment(self):
        param1 = 'Payment'
        self.update_redirect()
        return self.render_template('payment.html', param1=param1)



db.create_all()

""" Page View """
appbuilder.add_view(ProductPageView, 'Hit Product', category="Product")
appbuilder.add_link("Phone", href="/productpageview/phone/", category="Product")
appbuilder.add_view(PaymentPageView, 'payment', category="payment")


# Add a link
appbuilder.add_link("Facebook", href="https://www.facebook.com/BroadwayHK/", icon = "fa-facebook")
appbuilder.add_link("Promotions", href="https://www.broadwaylifestyle.com/promotions/")


appbuilder.add_view_no_menu(EmployeeHistoryView, "EmployeeHistoryView")
appbuilder.add_view(EmployeeView, "Employees", icon="fa-folder-open-o", category="Company")
appbuilder.add_separator("Company")
appbuilder.add_view(DepartmentView, "Departments", icon="fa-folder-open-o", category="Company")
appbuilder.add_view(FunctionView, "Functions", icon="fa-folder-open-o", category="Company")
appbuilder.add_view(BenefitView, "Benefits", icon="fa-folder-open-o", category="Company")
appbuilder.add_view(OrdersView, 'Order', category="Order")
appbuilder.add_view(OrderitemsView, 'List', category="Order items")
appbuilder.add_view(ProductsView, 'Product list', category="Control Panel")
appbuilder.add_view(BrandsView, 'Brands List', category="Control Panel")
appbuilder.add_view(SupplierView, 'Supplier', category="Control Panel")
appbuilder.add_view(InvoicesView, 'Invoices', category="Control Panel")
appbuilder.add_view(PaymentsView, 'Payments', category="Control Panel")
appbuilder.add_view(Delivery_addressView, 'Delivery_address', category="Control Panel")
appbuilder.add_view(CategoriesView, 'Categories', category="Control Panel")
appbuilder.add_view(BranchView, 'Branch', category="Control Panel")