from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, Docker!"
# Configure MongoDB connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Customers'
mongo = PyMongo(app)
# Define Customer model
class Customer:
    def __init__(self, customerId, customerName, customerMobile, customerAddress):
        self.customerId = customerId
        self.customerName = customerName
        self.customerMobile = customerMobile
        self.customerAddress = customerAddress
# Define CustomerService
class CustomerService:
    @staticmethod
    def add_customer(customer):
        customers = mongo.db.customers
        customers.insert_one({
            'customerId': customer.customerId,
            'customerName': customer.customerName,
            'customerMobile': customer.customerMobile,
            'customerAddress': customer.customerAddress
        })
        return jsonify({'message': 'Customer added successfully'})
    @staticmethod
    def get_all_customers():
        customers = mongo.db.customers
        result = []
        for customer in customers.find():
            result.append({
                'customerId': customer['customerId'],
                'customerName': customer['customerName'],
                'customerMobile': customer['customerMobile'],
                'customerAddress': customer['customerAddress']
            })
        return jsonify(result)
# Define routes
@app.route('/add_customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    customer = Customer(data['customerId'], data['customerName'], data['customerMobile'], data['customerAddress'])
    return CustomerService.add_customer(customer),201
@app.route('/get_all_customers', methods=['GET'])
def get_all_customers():
    return CustomerService.get_all_customers(),200
if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)