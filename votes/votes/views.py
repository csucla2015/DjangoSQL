from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import pymssql
def home2(request):

	conn = pymssql.connect(server='fejcz4m54q.database.windows.net', user='meet_bhagdev@fejcz4m54q', password='channelV1', database='meet_bhagdev')
	cursor = conn.cursor()
	query = str("""UPDATE votes SET value = value + 1 WHERE name = '""")+ str(request.POST['group1']) + str("""' """)
	print query
	cursor.execute(query)
	conn.commit()
	cursor.execute('SELECT * FROM votes')
	result = ""
	row = cursor.fetchone()
	while row:
	    result += str(row[0]) + str(" : ") + str(row[1]) + str(" votes")
	    result += str("\n")
	    row = cursor.fetchone()
	print result
	print request.POST['group1']
 	return render(
		request,
        	'/home/meet/DjangoProject/votes/templates/index2.html',
       		context_instance = RequestContext(request,
        	{
			"result" : result,
            		"value" : request.POST['group1']
        	})
    	)
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        '/home/meet/DjangoProject/votes/templates/index.html',
        context_instance = RequestContext(request,
        {

            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        '/home/meet/DjangoProject/votes/templates/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        '/home/meet/DjangoProject/votes/templates/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
