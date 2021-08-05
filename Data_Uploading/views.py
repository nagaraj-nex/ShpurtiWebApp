from django.db.models.fields import CharField
from django.shortcuts import render
import csv
import xlwt
from django.http import HttpResponse, request, response
from tablib import Dataset
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import Company_DataForm, UserProfileForm
from .models import Company_Data,Login
from .resources import Company_DataReasources
# Filter
from .filters import Company_DataFilter
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from .forms import SignUpForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
################################
from django.contrib.auth.forms import AuthenticationForm

def loginCheck(request):  # Login Page
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(request, username=username, password=password1)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
        
            return redirect('/show')
        else:
            messages.error(request, f'error while login, please try again')
            return redirect('login/')
    
    return render(request, 'Data_Uploading/login.html', {})


def download_excel_data(request):
    # content-type of response
    response = HttpResponse(content_type='application/ms-excel')

    # decide file name
    response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'

    # creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

    # adding sheet
    ws = wb.add_sheet("myfile")

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True

    # column header names, you can use your own headers here
    columns = ['Cid', 'Company_Name', 'Website', 'Employee_Range', 'Industry', 'Address_1', 'Address_2', 'City'
               'First_Name', 'Last_Name', 'Job_Title', 'LinkedIn_URL', 'Public_Profile', 'Email_Id', 'Contact_Num', 'Job_Url', 'Job_Opening']

    # write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    # get your data, from database or from a text file...
    company_data = Company_Data.objects.all()
    for my_row in company_data:
        row_num = row_num + 1

        ws.write(row_num, 0, my_row.cid, font_style)
        ws.write(row_num, 1, my_row.Company_Name, font_style)
        ws.write(row_num, 2, my_row.Website, font_style)
        ws.write(row_num, 3, my_row.Employee_Range, font_style)
        ws.write(row_num, 4, my_row.Industry, font_style)
        ws.write(row_num, 5, my_row.Address_1, font_style)
        ws.write(row_num, 6, my_row.Address_2, font_style)
        ws.write(row_num, 7, my_row.City, font_style)
        ws.write(row_num, 8, my_row.Zip_Code, font_style)
        ws.write(row_num, 9, my_row.First_Name, font_style)
        ws.write(row_num, 10, my_row.Last_Name, font_style)
        ws.write(row_num, 11, my_row.Job_Title, font_style)
        ws.write(row_num, 12, my_row.LinkedIn_URL, font_style)
        ws.write(row_num, 13, my_row.Public_Profile, font_style)
        ws.write(row_num, 14, my_row.Email_Id, font_style)
        ws.write(row_num, 15, my_row.Contact_Num, font_style)
        ws.write(row_num, 16, my_row.Job_Url, font_style)
        ws.write(row_num, 17, my_row.Job_Opening, font_style)

    wb.save(response)
    return response


def filter(request):
    company_data = Company_Data.objects.get
# company_data = Data.company_data_set.all()
    tfilter = Company_DataFilter(request.GET, queryset=company_data)
    return render(request, 'Data_Uploading/base.html', {'tfilter': tfilter}, {'company_data': company_data})


def main(request):
    return render(request, 'Data_Uploading/base.html')


@login_required
def simple_upload(request):
    if request.method == 'POST':
        company_dataresource = Company_DataReasources()
        dataset = Dataset()
        new_company_data = request.FILES['myfile']
        if not new_company_data.name.endswith("xlsx"):
            messages.info(request, 'wrong format of file')
            return render(request, 'Data_Uploading/upload.html')

        imported_data = dataset.load(new_company_data.read(), format="xlsx")
        for data in imported_data:

            value = Company_Data(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
                data[15],
                data[16],
                data[17],
                data[18],
                data[19],
                data[20],
                data[21],
                data[22],
                data[23],
                data[25],
                data[26],
                data[27],
                data[28],
                data[29],
                data[30],
                data[31],
                data[32],
                data[33],
                data[34]

            )
            value.save()
    return render(request, 'Data_Uploading/upload.html')  # upload.html


def search(request):
    # query=request.GET['query']
    # allPosts= Company_Data.objects.filter(Company_Name__icontains=query)
    # params={'allPosts': allPosts}
    query = request.GET['query']
    if len(query) > 78:
        allPosts = Company_Data.objects.none()
    else:
        allPostsCompany_Name = Company_Data.objects.filter(
            Company_Name__icontains=query)
        allPostsWebsite = Company_Data.objects.filter(Website__icontains=query)
        allPostsJob_Title = Company_Data.objects.filter(
            Job_Title__icontains=query)
        allPostsIndustry = Company_Data.objects.filter(
            Industry__icontains=query)
        allPostsCountry = Company_Data.objects.filter(Country__icontains=query)
        allPostsEmployee_Range = Company_Data.objects.filter(
            Employee_Range__icontains=query)
        allPosts = allPostsCompany_Name.union(
            allPostsWebsite, allPostsJob_Title, allPostsIndustry, allPostsCountry, allPostsEmployee_Range)
    if allPosts.count() == 0:
        messages.warning(
            request, "No search results found. Please refine your query.")
    params = {'allPosts': allPosts, 'query': query}
    # search_results.html
    return render(request, 'Data_Uploading/result1.html', params)


def company(request):
    if request.method == "POST":
        form = Company_DataForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('Data_Uploading/show')
            except:
                pass
    else:
        form = Company_Data()
    return render(request, 'Data_Uploading/index.html', {'form': form})


def show(request):
    Data = Company_Data.objects.all()
    return render(request, "Data_Uploading/show1.html", {'Data': Data})


def show1(request):
    return render(request, "Data_Uploading/show1.html")


def demo(request):
    return render(request, "Data_Uploading/demotbl.html")


def edit(request, id):
    Data = Company_Data.objects.get(id=id)
    return render(request, 'Data_Uploading/edit.html', {'Data': Data})


def update(request, id):
    Data = Company_Data.objects.get(id=id)
    form = Company_DataForm(request.POST, instance=Data)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'Data_Uploading/edit.html', {'Data': Data})


def destroy(request, id):
    Data = Company_Data.objects.get(id=id)
    Data.delete()
    return redirect("Data_Uploading/show", {'Data': Data})


@csrf_exempt
def login_user(request):  # Login Page
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'login success')
            if UserProfile.objects.filter(user=user).values('country').count() == 0:
                return redirect('/show')
            else:
                return redirect('/show2')
        else:
            messages.error(request, f'error while login, please try again')
            return redirect('login')
    else:
        return render(request, 'Data_Uploading/login.html', {})


@login_required
def logout_user(request):  # Contact Page
    logout(request)
    messages.success(request, f'logout successful')
    return redirect('login')


@csrf_exempt
def register_user(request):  # Register Page
    if request.method == "POST":
        
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form = SignUpForm(request.POST)
            form.save()
            return redirect('/thank_you')
        else:
            
            print(form.errors)
            messages.error(request, f'Please correct the error below.')
    else:
        form = SignUpForm()
    # return render(request, 'Data_Uploading/register.html', context={'form': form})
    return render(request, 'Data_Uploading/register1.html')


def thank_you(request):  # thank you page
    return render(request, 'Data_Uploading/thank_you.html', {})


def home(request):  # Home Page(domain.com)
    return render(request, 'Data_Uploading/home.html', {})

