print("BMI Calculator\n")
print("Scripted by HMAndro\n\n")

Weight=float(input("Enter weight in KG: "));
Height=float(input("Enter height in Centimeter: "));

BMI=Weight/Height**2*10000;
print("Your BMI is",BMI,".");

if (BMI <= 18.5):
    print("Underweight BMI",BMI)
    
elif (BMI >= 18.6 and BMI <=24.9):
    print("Normal BMI",BMI)
    
elif (BMI >= 25 and BMI <=29.9):
    print("Overweight BMI",BMI)
    
elif (BMI >= 30):
    print("Obese BMI",BMI)
# print
# print("Below 18.5","-","Underweight BMI");
# print("18.5","-","24.9","-","Normal BMI");
# print("25","-","29.9","-","Overweight BMI");
# print("30 and above","-","Obese BMI");
