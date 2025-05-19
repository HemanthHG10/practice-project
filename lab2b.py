def factorial(n):
	if n==0:
		return 1
	else:
		fact=1
		for i in range(1,n+1):
			fact*=i
		return fact

n = int(input("Enter the value of n(greater than 0)"))
r = int(input("Enter the value of r(greater than 0 and less than or equals to n)"))
binomialCoefficients=factorial(n)/(factorial(r)*factorial(n-r))
print("The binomial Coefficient is:",binomialCoefficients)