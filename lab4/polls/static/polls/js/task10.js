
//10 функция

    function Car(brand) { // prototype proto
        this._brand = brand;
    }

    Object.defineProperty(Car.prototype, 'brand', {
        get: function () {
            return 'brand = ${this._brand}';
        },
        set: function (brand) {
            this._brand = brand;
        }
    });

    function Truck(lifting, brand) {
        Car.call(this, brand);
        this.lifting = lifting;
    }

    Truck.prototype = Object.create(Car.prototype);

    Object.defineProperty(Car.prototype, 'lifting', {
        get: function () {
            return 'lifting  = ${this.lifting}';
        },
        set: function (lifting) {
            this.lifting = lifting;
        }
    });

    Truck.prototype.showLifting = function () {
        return `lifting: ${this.lifting}`;
    };

    function DecoratorShowLifting(func) {
        return function () {
            let str = func.call(this);
            return '(Called with decorator) ' + str;
        }
    }


//10 классы


    class Car {
        constructor(brand) {
            this._brand = brand;
        }
        get brand() {
            return 'brand = ${this._brand}';
        }
        set brand(brand) {
            this._square = brand;
        }
    }

    class Truck extends Car {
        constructor(brand, lifting) {
            super(brand);
            this._lifting = lifting;
        }

        get lifting() {
            return lifting;
        }

        set lifting(lifting) {
            this._lifting = lifting;
        };

    }
    function DecoratorShowLifting(func) {
        return function() {
            let price = func.call(this);
            return '(Called with decorator)'  + lifting;
        }
    }