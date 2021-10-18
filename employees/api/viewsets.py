from rest_framework.viewsets import ModelViewSet
from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import action
from django.http.response import JsonResponse
from datetime import date
from dateutil.relativedelta import relativedelta
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class EmployeeViewSet(ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = [
        'id',
        'name',
        'email',
        'department',
        'salary',
        'birth_date'
    ]
    
    @action(methods=['get'], detail=False)
    def age(self, request):
        younger_employee = Employee.objects.order_by('birth_date').last()
        younger_employee_query = self.get_queryset().filter(birth_date=younger_employee.birth_date)
        older_employee = Employee.objects.order_by('birth_date').first()
        older_employee_query = self.get_queryset().filter(birth_date=older_employee.birth_date)
        employees = Employee.objects.all()
        ages = []
        for employee in employees:
            try:
                today = date.today()
                time_difference = relativedelta(today, employee.birth_date)
                age = time_difference.years
            except:
                age = None
            ages.append(age)
        average = sum(ages) / len(ages)
        younger_serializer = self.get_serializer(younger_employee_query, many=True)
        older_serializer = self.get_serializer(older_employee_query, many=True)

        return JsonResponse({'Younger':younger_serializer.data, 'Older':older_serializer.data, 'Average':average}, content_type="application/json")
    
    @action(methods=['get'], detail=False)
    def salary(self, request):
        lowest_salary_employee = Employee.objects.order_by('salary').first()
        lowest_salary_employee_query = self.get_queryset().filter(salary=lowest_salary_employee.salary)
        highest_salary_employee = Employee.objects.order_by('salary').last()
        highest_salary_employee_query = self.get_queryset().filter(salary=highest_salary_employee.salary)
        employees = Employee.objects.all()
        salaries = []
        for employee in employees:
            if employee.salary != None:
                salaries.append(employee.salary)
        average = sum(salaries) / len(salaries)
        lowest_salary_serializer = self.get_serializer(lowest_salary_employee_query, many=True)
        highest_salary_serializer = self.get_serializer(highest_salary_employee_query, many=True)

        return JsonResponse({'Lowest':lowest_salary_serializer.data, 'Highest':highest_salary_serializer.data, 'Average':average}, content_type="application/json")