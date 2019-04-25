# NatePy
I like python as a language because of how easy it is to use, but I do not like a lot of things about python's syntax.
To make python easier for me to use, I have created this python script that can be used to convert how I think python should be written (similar to many other languages like Java, C++, C#, etc.) into a form that python can actually execute.
Using this transpiler, you can transpile a .npy file to a .py file. This allows for:
- semicolons
- curly braces
- incrementers/decrementers
- "else if"
- "//" comments

This will transpile a file that looks something like this (.npy)
    // Name: Nathan Gawith
    // Class: COMPSCI101 Problem Solving & Programing I FS2017
    // Assignment: Real Estate Agent Application (Assignment #2)
    // Creation Date: September 22nd, 2017
    // Due Date: September 29th, 2017
    
    //function used to calculate the monthly payment
    def calMonthlyPayment(price, down_payment, years, interest_rate) {
        numerator = (price - down_payment) * ((1 + interest_rate) ** years);
        denominator = 12 * years;
        return numerator / denominator;
    }
    
    //function used to calculate the toatl interest
    def calTotalInterest(price, down_payment, years, monthly_payment) {
        minuend = monthly_payment * years * 12;
        subtrahend = price - down_payment;
        return minuend - subtrahend;
    }
        
    //function containing the main application
    def application() {
        //Initialization of variables
        price = 0;
        down_payment = False;
        credit_score = 0;
        interest_rate = 0;
        //Prompting the user to enter price of dream home
        while (True) {
            try {
                price = int(input('Enter the price of your dreams house : $'));
                if (price < 0) {
                    print('House price must be a positive number only');
                }
                else {
                    break;
                }
            }
            except {
                print('House price must be a positive number only');
            }
        }
        //Prompting the user to enter down payment
        while (True) {
            down_payment = input('Are you making any down payments? ');
            if (down_payment.lower() == 'yes') {
                while (True) {
                    try {
                        down_payment = int(input('How much is your down payment? $'));
                        if (down_payment < 0) {
                            print('Down payment must be a positive number only');
                        }
                        else if (down_payment >= price) {
                            print('Down payment must be less than the house price');
                        }
                        else {
                            break
                        }
                    }
                    except {
                        print('House price must be a positive number only');
                    }
                }
                break
            }
            else if (down_payment.lower() == 'no') {
                down_payment = 0;
                break;
            }
            else {
                print('Please enter only \'yes\' or \'no\'');
            }
        }
        //Prompting the user to enter credit score
        while (True) {
            try {
                credit_score = int(input('Please enter your credit score : '));
                if (credit_score >= 0) {
                    if (credit_score >= 0 and credit_score <= 500) {
                        interest_rate = 0.05;
                    }
                    else if (credit_score >= 501 and credit_score <= 700) {
                        interest_rate = 0.02;
                    }
                    else {
                        interest_rate = 0.01;
                    }
                    print('\nBased on your Credit Score, your interest rate is : {}\n'.format(interest_rate));
                    break;
                }
            }
            except {
                print('', end ='');
            }
        }
        //for loop used to print the monthly payments and total interest for 10 - 25 years
        for years in range(10, 26) {
            monthly_payment = calMonthlyPayment(price, down_payment, years, interest_rate);
            total_interest = calTotalInterest(price, down_payment, years, monthly_payment);
            print('Pay in {0} years. Monthly payment is ${1:.2f} Total interest is ${2:.2f}'.format(years, monthly_payment, total_interest));
        }
    }
    //Greeting to user
    print('Welcome to interest calculator program');
    //Starts the main application
    application();
    //while loop used to ask the user to run the application again or not
    while (True) {
        rerun = input('Would you like to use the application again?? ');
        if (rerun.lower() == 'yes') {
            application();
        }
        else if (rerun.lower() == 'no') {
            print('\nThanks for using Interest Calculator application!');
            break;
        }
        else {
            print('Please enter only \'yes\' to run again or \'no\' to exit.');
        }
    }
Into a working python script like this
    # Name: Nathan Gawith
    # Class: COMPSCI101 Problem Solving & Programing I FS2017
    # Assignment: Real Estate Agent Application (Assignment #2)
    # Creation Date: September 22nd, 2017
    # Due Date: September 29th, 2017
    #function used to calculate the monthly payment
    def calMonthlyPayment(price, down_payment, years, interest_rate):
        numerator = (price - down_payment) * ((1 + interest_rate) ** years)
        denominator = 12 * years
        return numerator / denominator
    #function used to calculate the toatl interest
    def calTotalInterest(price, down_payment, years, monthly_payment):
        minuend = monthly_payment * years * 12
        subtrahend = price - down_payment
        return minuend - subtrahend
    #function containing the main application
    def application():
        #Initialization of variables
        price = 0
        down_payment = False
        credit_score = 0
        interest_rate = 0
        #Prompting the user to enter price of dream home
        while (True):
            try:
                price = int(input('Enter the price of your dreams house : $'))
                if (price < 0):
                    print('House price must be a positive number only')
                else:
                    break
            except:
                print('House price must be a positive number only')
        #Prompting the user to enter down payment
        while (True):
            down_payment = input('Are you making any down payments? ')
            if (down_payment.lower() == 'yes'):
                while (True):
                    try:
                        down_payment = int(input('How much is your down payment? $'))
                        if (down_payment < 0):
                            print('Down payment must be a positive number only')
                        elif (down_payment >= price):
                            print('Down payment must be less than the house price')
                        else:
                            break
                    except:
                        print('House price must be a positive number only')
                break
            elif (down_payment.lower() == 'no'):
                down_payment = 0
                break
            else:
                print('Please enter only \'yes\' or \'no\'')
        #Prompting the user to enter credit score
        while (True):
            try:
                credit_score = int(input('Please enter your credit score : '))
                if (credit_score >= 0):
                    if (credit_score >= 0 and credit_score <= 500):
                        interest_rate = 0.05
                    elif (credit_score >= 501 and credit_score <= 700):
                        interest_rate = 0.02
                    else:
                        interest_rate = 0.01
                    print('\nBased on your Credit Score, your interest rate is : {}\n'.format(interest_rate))
                    break
            except:
                print('', end ='')
        #for loop used to print the monthly payments and total interest for 10 - 25 years
        for years in range(10, 26):
            monthly_payment = calMonthlyPayment(price, down_payment, years, interest_rate)
            total_interest = calTotalInterest(price, down_payment, years, monthly_payment)
            print('Pay in {0} years. Monthly payment is ${1:.2f} Total interest is ${2:.2f}'.format(years, monthly_payment, total_interest))
    #Greeting to user
    print('Welcome to interest calculator program')
    #Starts the main application
    application()
    #while loop used to ask the user to run the application again or not
    while (True):
        rerun = input('Would you like to use the application again?? ')
        if (rerun.lower() == 'yes'):
            application()
        elif (rerun.lower() == 'no'):
            print('\nThanks for using Interest Calculator application!')
            break
        else:
            print('Please enter only \'yes\' to run again or \'no\' to exit.')
