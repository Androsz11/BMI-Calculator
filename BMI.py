print("BMI Calculator")
print
print("Scripted by HMAndro")
print
print
Weight=int(input("Enter weight in KG"));
Height=int(input("Enter height in Centimeter"));
BMI=Weight/Height**2*10000;
print("Your BMI is",BMI,".");
print
print("Below 18.5","-","Underweight BMI");
print("18.5","-","24.9","-","Normal BMI");
print("25","-","29.9","-","Overweight BMI");
print("30 and above","-","Obese BMI");
