from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, 'main/home.html')

def calculate(request):
    if request.method == "POST":
        numbers = request.POST.getlist('numbers')
        operation = request.POST.get('operation')
        
        
        try:
            numbers = [float(num) for num in numbers if num]
        except ValueError:
            return render(request, 'main/home.html', {'error': 'Please enter valid numbers'})

        if not numbers:
            return render(request, 'main/home.html', {'error': 'Please enter at least one number'})

        
        result = None
        if operation == 'addition':
            result = sum(numbers)
        elif operation == 'subtraction':
            result = numbers[0] - sum(numbers[1:])
        elif operation == 'multiplication':
            result = 1
            for num in numbers:
                result *= num
        elif operation == 'division':
            try:
                result = numbers[0]
                for num in numbers[1:]:
                    result /= num
            except ZeroDivisionError:
                return render(request, 'main/home.html', {'error': 'Division by zero is not allowed'})
        

        
        return render(request, 'main/home.html', {'result': result})

    return render(request, 'main/home.html')
