from flask import Flask, render_template, request

app = Flask(__name__)
my_cars = [
    {"id": 1, "brand": "Toyota", "model": "Corolla", "year": 2020},
    {"id": 2, "brand": "Honda", "model": "Civic", "year": 2018},
    {"id": 3, "brand": "Ford", "model": "Mustang", "year": 2021},
    {"id": 4, "brand": "Chevrolet", "model": "Malibu", "year": 2019},
    {"id": 5, "brand": "BMW", "model": "3 Series", "year": 2022},
    {"id": 6, "brand": "Audi", "model": "A4", "year": 2020},
    {"id": 7, "brand": "Mercedes-Benz", "model": "C-Class", "year": 2021},
    {"id": 8, "brand": "Hyundai", "model": "Elantra", "year": 2017},
    {"id": 9, "brand": "Nissan", "model": "Altima", "year": 2020},
    {"id": 10, "brand": "Volkswagen", "model": "Jetta", "year": 2019}
]
# R - read
@app.route("/")
def home():
        return render_template("index.html", cars=my_cars)
      
# C - create
@app.route("/add", methods=['GET','POST'])
def add():
        if request.method == 'GET':
            return render_template("add.html")
        else: #POST
            
            data = request.get_json()
            brand = data.get('brand')
            model = data.get('model')
            year = data.get('year')
            my_cars.append({"id": len(my_cars)+1, "brand": brand,"model":model, "year" :year},)
            return render_template('index.html', cars=my_cars)
# U - update
@app.route("/upd/<id>" ,methods=['GET',"PUT"])
def update(id=0):
    data = request.get_json()
    brand = data.get('brand')
    model = data.get('model')
    year = data.get('year')
    car_to_update=next((car for car in my_cars if car["id"] == int(id)), None)
    if car_to_update:
         car_to_update['brand']=brand
         car_to_update['model']=model
         car_to_update['year']=year
    return render_template('index.html', cars=my_cars)
# D -delete
@app.route("/del/<id>" ,methods=['GET',"DELETE"])
def  delete(id=0):
    car_to_remove=next((car for car in my_cars if car["id"] == int(id)), None)
    if car_to_remove: my_cars.remove(car_to_remove)
    return render_template('index.html', cars=my_cars) 
