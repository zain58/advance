import numpy as np 
from django.shortcuts import render
from django.http import HttpResponse
from . import newLoad

# index
def homepage(request):
    return render(request, 'index.html',{'title': 'HOME- ADVANCE BULLETIN'},)
    
# home
def Home(request):
    data1 = newLoad.dfN
    data2 = newLoad.dfA
    dtlist = []
    data = []
    htmlA=''; htmlN=''; categoryA=''; categoryN= '';
#NewsONE Pakistan
    for index, row in data1.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)
        # print(push)
        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'Pakistan':
            categoryN += "<h2 style='color:black' >" + ident +"</h2>"

    for index, row in data1.iterrows():
        if row['category'] == 'Pakistan':
            imgurl=str(row['img-url'])
            htmlA += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
        else: 
            row['category']
#ARY Pakistan
    for index, row in data2.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)
        # print(push)
        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'PAKISTAN':
            categoryA += "<h2 style='color:black' >" + ident +"</h2>"
    for index, row in data2.iterrows():
         if row['category'] == 'PAKISTAN':
            imgurl=str(row['img-url'])
            htmlN += "<div class='card' style='margin:2em; width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"

    return render(request, 'home.html', {'title': 'HOME- ADVANCE BULLETIN','h1': 'Breaking', 'categA': categoryA, 'categN':categoryN,'htmlA':htmlA,'htmlN':htmlN},)

#Ary
def ary(request):

#for Pakistan

    data2 = newLoad.dfA
    dtlist = []
    data = []
    html1='';  category = ''; updates = '';
    for index, row in data2.iterrows():
        if row['category'] == 'PAKISTAN':
            imgurl=str(row['img-url'])


            html1 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in data2.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'PAKISTAN':
            category += "<h2 style='color:black' >" + ident +"</h2>"

#for international




    data3 = newLoad.dfA
    dtlist1 = []
    data1 = []
    html2 = '' ; category1 = ''; updates = '';
    for index, row in data3.iterrows():
        if row['category'] == 'INTERNATIONAL':
            imgurl1=str(row['img-url'])


            html2 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl1 if imgurl1!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in data3.iterrows():
        dt3=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist1.append(dt3[3])
    # function to get unique values
    def unique(dtlist1):
        cate1 = np.array(dtlist1)
        push1 = np.unique(cate1)

        return data1.extend(push1)
    unique(dtlist1)
    data1.sort()
    for ident1 in data1:
        if ident1 == 'INTERNATIONAL':
            category1 += "<h2 style='color:black' >" + ident1 +"</h2>"


#for bussiness
    data4 = newLoad.dfA
    dtlist2 = []
    data2 = []
    html3 = '' ; category2 = ''; updates = '';
    for index, row in data4.iterrows():
        if row['category'] == 'BUSINESS':
            imgurl2=str(row['img-url'])


            html3 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl2 if imgurl2!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in data4.iterrows():
        dt4=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist2.append(dt4[3])
    # function to get unique values
    def unique(dtlist2):
        cate2 = np.array(dtlist2)
        push2 = np.unique(cate2)

        return data2.extend(push2)
    unique(dtlist2)
    data2.sort()
    for ident2 in data2:
        if ident2 == 'BUSINESS':
            category2 += "<h2 style='color:black' >" + ident2 +"</h2>"


#for SCI & TECH



    data5 = newLoad.dfA
    dtlist3 = []
    data3 = []
    html4 = '' ; category3 = ''; updates = '';
    for index, row in data5.iterrows():
        if row['category'] == 'SCI & TECH':
            imgurl3=str(row['img-url'])


            html4 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl3 if imgurl3!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in data5.iterrows():
        dt5=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist3.append(dt5[3])
    # function to get unique values
    def unique(dtlist3):
        cate3 = np.array(dtlist3)
        push3 = np.unique(cate3)

        return data3.extend(push3)
    unique(dtlist3)
    data3.sort()
    for ident3 in data3:
        if ident3 == 'SCI & TECH':
            category3 += "<h2 style='color:black' >" + ident3 +"</h2>"


#for LIFESTYLE


    data6 = newLoad.dfA
    dtlist4 = []
    data4 = []
    html5 = '' ; category4 = ''; updates = '';
    for index, row in data6.iterrows():
        if row['category'] == 'LIFESTYLE':
            imgurl4=str(row['img-url'])


            html5 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl4 if imgurl4!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in data6.iterrows():
        dt6=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist4.append(dt6[3])
    # function to get unique values
    def unique(dtlist4):
        cate4 = np.array(dtlist4)
        push4 = np.unique(cate4)

        return data4.extend(push4)
    unique(dtlist4)
    data4.sort()
    for ident4 in data4:
        if ident4 == 'LIFESTYLE':
            category4 += "<h2 style='color:black' >" + ident4 +"</h2>"


#for health

    data7 = newLoad.dfA
    dtlist5 = []
    data5 = []
    html6 = '' ; category5 = ''; updates = '';
    for index, row in data7.iterrows():
        if row['category'] == 'HEALTH':
            imgurl5=str(row['img-url'])


            html6 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl5 if imgurl5!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in data7.iterrows():
        dt7=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist5.append(dt7[3])
    # function to get unique values
    def unique(dtlist5):
        cate5 = np.array(dtlist5)
        push5 = np.unique(cate5)

        return data5.extend(push5)
    unique(dtlist5)
    data5.sort()
    for ident5 in data5:
        if ident5 == 'HEALTH':
            category5 += "<h2 style='color:black' >" + ident5 +"</h2>"



    return render(request, 'ARY.html', {'title': 'HOME- ARY', 'h1': 'ARY' , 'categ': category,'categ1':category1 , 'categ2':category2, 'categ3':category3, 'categ4':category4, 'categ5':category5 , 'html':html1, 'html1':html2 , 'html2':html3 , 'html3':html4 , 'html4':html5, 'html5': html6})





#NEWSONE
def newsone(request):
    dataN = newLoad.dfN
#for Pakistan
    dtlist = []
    data = []
    html ='';  category = ''; updates = '';
    for index, row in dataN.iterrows():
        if row['category'] == 'Pakistan':
            imgurl=str(row['img-url'])


            html += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataN.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)
        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'Pakistan':
            category += "<h2 style='color:black' >" + ident +"</h2>" 

#for world
    dataN1 = newLoad.dfN
    dtlist = []
    data = []
    html1='';  category1 = ''; updates = '';
    for index, row in dataN1.iterrows():
        if row['category'] == 'World':
            imgurl=str(row['img-url'])


            html1 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataN1.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'World':
            category1 += "<h2 style='color:black' >" + ident +"</h2>"

#for psl 2019
    dataN2 = newLoad.dfN
    dtlist = []
    data = []
    html2='';  category2 = ''; updates = '';
    for index, row in dataN2.iterrows():
        if row['category'] == 'WORLD CUP 2019':
            imgurl=str(row['img-url'])


            html2 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataN2.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'WORLD CUP 2019':
            category2 += "<h2 style='color:black' >" + ident +"</h2>"

#for Sports
    dataN3 = newLoad.dfN
    dtlist = []
    data = []
    html3='';  category3 = ''; updates = '';
    for index, row in dataN3.iterrows():
        if row['category'] == 'Sports':
            imgurl=str(row['img-url'])


            html3 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataN3.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'Sports':
            category3 += "<h2 style='color:black' >" + ident +"</h2>"

#for Business
    dataN4 = newLoad.dfN
    dtlist = []
    data = []
    html4='';  category4 = ''; updates = '';
    for index, row in dataN4.iterrows():
        if row['category'] == 'Business':
            imgurl=str(row['img-url'])


            html4 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataN4.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'Business':
            category4 += "<h2 style='color:black' >" + ident +"</h2>"
#for Entertainment
    dataN5 = newLoad.dfN
    dtlist = []
    data = []
    html5='';  category5 = ''; updates = '';
    for index, row in dataN5.iterrows():
        if row['category'] == 'Entertainment':
            imgurl=str(row['img-url'])


            html5 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataN5.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'Entertainment':
            category5 += "<h2 style='color:black' >" + ident +"</h2>"
#for Tech
    dataN6 = newLoad.dfN
    dtlist = []
    data = []
    html6='';  category6 = ''; updates = '';
    for index, row in dataN6.iterrows():
        if row['category'] == 'Technology ':
            imgurl=str(row['img-url'])


            html6 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataN6.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'Technology ':
            category6 += "<h2 style='color:black' >" + ident +"</h2>"

#for Special
    dataN7 = newLoad.dfN
    dtlist = []
    data = []
    html7='';  category7 = ''; updates = '';
    for index, row in dataN7.iterrows():
        if row['category'] == 'Special':
            imgurl=str(row['img-url'])


            html7 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataN7.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'Special':
            category7 += "<h2 style='color:black' >" + ident +"</h2>"

#for Lifestyle
    dataN8 = newLoad.dfN
    dtlist = []
    data = []
    life ='';  category8 = ''; updates = '';
    for index, row in dataN8.iterrows():
        if row['category'] == 'Lifestyle ':
            imgurl=str(row['img-url'])
            

            life += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataN8.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'Lifestyle ':
            category8 += "<h2 style='color:black' >" + ident +"</h2>"
    return render(request, 'NewsOne.html', {'title': 'HOME- NEWSONE', 'h1': 'NEWSONE', 'categ': category,'html':html, 'categ1': category1,'html1':html1,'categ2': category2,'html2':html2,'categ3': category3,'html3':html3,'categ4': category4,'html4':html4,'categ5': category5,'html5':html5,'categ6': category6,'html6':html6,'categ7': category7,'html7':html7,'categ8': category8,'html8':life,})

#Dunya
def dunya(request):
#for Pakistan
    dataD = newLoad.dfD
    dtlist = []
    data = []
    html ='';  category = ''; updates = '';
    for index, row in dataD.iterrows():
        if row['category'] == 'Pakistan':
            imgurl=str(row['img-url'])


            html += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataD.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)
        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'Pakistan':
            category += "<h2 style='color:black' >" + ident +"</h2>" 

#for world
    dataD1 = newLoad.dfD
    dtlist = []
    data = []
    html1='';  category1 = ''; updates = '';
    for index, row in dataD1.iterrows():
        if row['category'] == 'world':
            imgurl=str(row['img-url'])


            html1 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataD1.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'world':
            category1 += "<h2 style='color:black' >" + ident +"</h2>"

#for business
    dataD2 = newLoad.dfD
    dtlist = []
    data = []
    html2='';  category2 = ''; updates = '';
    for index, row in dataD2.iterrows():
        if row['category'] == 'business':
            imgurl=str(row['img-url'])


            html2 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataD2.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'business':
            category2 += "<h2 style='color:black' >" + ident +"</h2>"

#for circket
    dataD3 = newLoad.dfD
    dtlist = []
    data = []
    html3='';  category3 = ''; updates = '';
    for index, row in dataD3.iterrows():
        if row['category'] == 'circket':
            imgurl=str(row['img-url'])


            html3 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataD3.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'circket':
            category3 += "<h2 style='color:black' >" + ident +"</h2>"

#for entertainment
    dataD4 = newLoad.dfD
    dtlist = []
    data = []
    html4='';  category4 = ''; updates = '';
    for index, row in dataD4.iterrows():
        if row['category'] == 'entertainment':
            imgurl=str(row['img-url'])


            html4 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataD4.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'entertainment':
            category4 += "<h2 style='color:black' >" + ident +"</h2>"
#for Tech
    dataD5 = newLoad.dfD
    dtlist = []
    data = []
    html5='';  category5 = ''; updates = '';
    for index, row in dataD5.iterrows():
        if row['category'] == 'Technology':
            imgurl=str(row['img-url'])


            html5 += "<div class='card' style='margin:2em;width:18em'><img class='card-img-top' src='" + (imgurl if imgurl!="nan" else "http://127.0.0.1:8000/static/images/newsworld.png") + "' alt='Card image cap'><h5 class='card-title'>" + row['title'] + "</h5><div class='card-block'><p class='card-text' style='font-weight: bolder;'>" + row['summery']+ "</p>"+"<div class='card-footer'><p style='font-weight: bolder;'> Opinion </p><small class='text-muted' style='font-weight: bolder;'>"+row['opinion']+"</small></div></div></div>"
    for index, row in dataD5.iterrows():
        dt2=index, row['title'], row['img-url'], row['category'],row['summery'],row['opinion']
        dtlist.append(dt2[3])
    # function to get unique values
    def unique(dtlist):
        cate = np.array(dtlist)
        push = np.unique(cate)

        return data.extend(push)
    unique(dtlist)
    data.sort()
    for ident in data:
        if ident == 'Technology':
            category5 += "<h2 style='color:black' >" + ident +"</h2>"
    return render(request, 'dunya.html', {'title': 'HOME- Dunya', 'h1': 'Dunya', 'categ': category,'html':html, 'categ1': category1,'html1':html1,'categ2': category2,'html2':html2,'categ3': category3,'html3':html3,'categ4': category4,'html4':html4,'categ5': category5,'html5':html5,})

#About
# def about(request):
	# return render(request, 'about.html', {'title': 'About'},)