from django.db.models.fields import CharField
from django.shortcuts import render
import csv
# Create your views here.
from django.http import HttpResponse, request, response
from tablib import Dataset
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import Company_DataForm
from .models import Company_Data
from .resources import Company_DataReasources
# Filter
from .filters import Company_DataFilter


def filter(request):
    company_data = Company_Data.objects.get
#company_data = Data.company_data_set.all()
    tfilter = Company_DataFilter(request.GET, queryset=company_data)
    return render(request, 'Data_Uploading/base.html', {'tfilter': tfilter}, {'company_data': company_data})


def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    company_data = Company_Data.objects.all()
    writer = csv.writer(response)
    for data in company_data:
        writer.writerow(['data.cid', 'data.Company_Name', 'data.Website', 'data.Employee_Range', 'data.Industry',
                         'data.Address_1', 'data.Address_2', 'data.City',
                         'data.Zip_Code', 'data.Country', 'data.First_Name',
                         'data.Last_Name', 'data.Job_Title', 'data.LinkedIn_UR',
                         'data.Public_Profile', 'data.Email_Id',
                         'data.Contact_Num', 'data.Job_Url', 'data.Job_Opening'])
    return response


def main(request):
    return render(request, 'Data_Uploading/base.html')


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
                data[18]
            )
            value.save()
    return render(request, 'Data_Uploading/upload1.html')  # upload.html

# searchview


def search(request):
    # query=request.GET['query']
    #allPosts= Company_Data.objects.filter(Company_Name__icontains=query)
    #params={'allPosts': allPosts}
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
        return redirect("Data_Uploading/show")
    return render(request, 'Data_Uploading/edit.html', {'Data': Data})


def destroy(request, id):
    Data = Company_Data.objects.get(id=id)
    Data.delete()
    return redirect("Data_Uploading/show")
