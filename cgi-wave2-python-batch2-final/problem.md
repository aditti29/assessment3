# CGI Core Track Flask API - Coding Challenge - III
​
## Objective
​
- In this case study, you have to create a simple Flask API web application where you should be able to add customer,view all customers. 
​
- Create API gateway and access the REST APIs through it.  
​
- The APIs ( access through gateway ) should be tested through Postman. Screenshot should be captured and shared. 
​
- Dockerize all the services ( creation of Dockerfile and Docker-compose). Share the screenshot showing the services are up and running ( use docker ps command)
​
## Following are the steps:
	
- Define the model class Customer with the following Properties
​
			- customerId : int
			- customerName : String
			- customerMobile : String
			- customerAddress : String
​
- Configure the connection properties for Mongo DB database 
    
​
-  Define CustomerServiceImpl implementing all the methods of CustomerService
​
        - add customer
        - get all customers
    
- Define the Customercontroller class and implement methods to create REST web service APIs based on 
        the methods defined in Customer Service
​
        HttpStatuses for 
            - add customer
                - code : 201 for successful addition
                - code : 409 if the user already exists
            - get all customers
                - code : 200 for successful
​
- Create API gateway and access the above REST APIs through that
​
- Dockerize the above services
​
MUST DO:
​
- Test the REST APIs using postman and share the screenshots of them
- Share the screenshot showing the containers are running
