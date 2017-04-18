from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from snippets.models import *
import datetime
from datetime import *
import  random
from django.db.models import Max
# import phonenumbers as pn

def UserSignUp(request):
	#print "qwert"
	if request.method == "POST":

		uname = request.POST.get('uname')
		print uname
		mobile = request.POST.get('mobile')
		print mobile
		tym = datetime.today()
		tym_temp = datetime.today() + timedelta(minutes = 30)

		try:
			mob = Temp.objects.get(mobile_temp=mobile)
			my_id = mob.id
			print my_id
			return HttpResponse("you have already entered your detail . please verify your otp." )
			


			# return HttpResponseRedirect('/snippets/'+str(my_id)+'/')

		except:

			ob_temp = Temp()
			ob_temp.uname = uname
			ob_temp.mobile_temp = mobile
			ob_temp.time_temp = tym_temp
			print ob_temp.time_temp
			ob_temp.save()
		# if user will try to resend otp and try to enter more than 4 time he will be blocked
		s=Temp.objects.filter(mobile_temp=mobile)
		g = [p.id for p in s]
		id_temp=max(g)
		print id_temp
		# v=len(s)
		# d = [p.time_temp for p in s]
		# time_first = d[0]
		# tym1_current = datetime.today()
		# print str(tym1_current)
		# # if ((v>3) and (tym1>=tym)):
		# # 	return render (request,"snippets/welcome.html") 
		# if ((v>4) and (int(tym1_current.strftime("%s")))<=(int(time_first.strftime("%s")))):
				
		# 	tym2 = datetime.today()
		# 	ob_block = Block()
		# 	ob_block.uname = uname
		# 	ob_block.mobile = mobile
		# 	ob_block.time_active = tym2
		# 	ob_block.save()
		# 	return HttpResponse("you will be blocked for one min")
		# 	# return HttpResponse("you will be blocked for half an hour")
		# if (v>4):	
		# 	my_mob = Block.objects.get(mobile = mobile)
		# 	my_time = my_mob.time_active
		# 	t1 = (int(tym1_current.strftime("%s")))-(int(my_time.strftime("%s")))

		# 	if(t1>=0):
		# 		return render (request,"snippets/welcome.html")


		# try:
		# 	mobile = Userinfo.objects.get(mobile = int(mobile))
		# 	return {'msg':'user is already exist with this mobile.'}, 400
		# except:
		# 	pass
		# getting all the data of a particular feild
		queryset = Userinfo.objects.all()
		d = [p.mobile for p in queryset]
		for e in d:
			if(e == int(mobile)):
				return HttpResponse("you are login with the same number")

			

		

		acti_time = datetime.today() + timedelta(minutes = 30)
		print acti_time
		q = Temp.objects.get(pk = id_temp)
		
		ob_mobile = Mobile()
		# activate_mobile.myuser = myuser
		ob_mobile.otp = random.randint(100000,999999)
		print ob_mobile.otp
		ob_mobile.valid_till = acti_time

		ob_mobile.temp = q
		
		ob_mobile.save()
			
	    	
				
		return HttpResponseRedirect('/snippets/'+str(id_temp)+'/')			
				
				#send verification code on mobile
				# from twilio.rest import TwilioRestClient 
				# client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN) 
				# client.messages.create(
				# 	to=mobile, 
				# 	from_=" ", 
				# 	body=" " +activate_mobile.otp.__str__(),  
				#)
			
			

				
				
				
		# except Exception, e:
		# 	return HttpResponse("here is errors")
	# else :
	# 		return HttpResponseRedirect('otp') 	


		#template = loader.get_template('snippets/registration.html')
	# 	context = {
	# 	'msg': 'yoe are registered',
	# }
	# 	return HttpResponse(template.render(context,request))
	return render (request,"snippets/registration.html")	
def OTP(request,temp_id):
	print "in otp"
	qn = Mobile.objects.filter(temp__id = temp_id)
	# print qn.temp_id
	g = [p.temp_id for p in qn]
	my_id = g[0]
	v=len(g)


	# taking the first time when the user entered

	time_f = Temp.objects.get(id = temp_id)
	time_first = time_f.time_temp
	uname = time_f.uname
	mobile = time_f.mobile_temp

	tym1_current = datetime.today()
	print str(tym1_current)

	# if ((v>3) and (tym1>=tym)):
	# 	return render (request,"snippets/welcome.html") 
	if ((v>2) and (int(tym1_current.strftime("%s")))<=(int(time_first.strftime("%s")))):
			
		
		ob_block = Block()
		print str(mobile) +"in block"+ str(uname)
		tym2 = datetime.today()
		ob_block.uname = uname
		ob_block.mobile = mobile
		ob_block.time_active = tym2
		ob_block.save()
		return HttpResponse("you will be blocked for one thirty minutes")
		# return HttpResponse("you will be blocked for half an hour")
	if (v>2):	
		my_mob = Block.objects.get(mobile = mobile)
		my_time = my_mob.time_active
		t1 = (int(tym1_current.strftime("%s")))-(int(my_time.strftime("%s")))

		if(t1>=0):
			return render (request,"snippets/welcome.html")




	if request.method == "POST":
		print "hello"
		# s=Mobile.objects.all().aggregate(Max('id'))
		# k = s['id__max']
		# print k
		# ty = Mobile.objects.get(id=k)
		# print ty.otp
		# otp = ty.otp

		# get the value from the foreign key
		# qn = Mobile.objects.filter(temp__id=temp_id)
		qn = Mobile.objects.filter(temp__id = temp_id)
		# print qn.temp_id
		g = [p.id for p in qn]
		max_id =  max(g)
		print max_id
		my_id1 = Mobile.objects.get(id=max_id)
		print my_id1.otp

		otp = my_id1.otp
		print otp
		my_otp = request.POST.get('otp')

		print my_otp
		if(int(my_otp)==int(otp)):
			print "jkjk"
			
			s = Temp.objects.get(id = temp_id)
			my_name = s.uname
			my_mobile = s.mobile_temp
			ob_user = Userinfo()
			ob_user.uname = my_name
			ob_user.mobile = my_mobile
			ob_user.save()
			return HttpResponse("your otp is same and u are registered")
			# return HttpResponseRedirect('/snippets/'+login+'/')


		else:
			
			return HttpResponse("you have entered a wrong otp")		
	return render(request,"snippets/otp.html",{"my_id":my_id} )





# Create your views here.
def Login(request):
	if request.method == "POST":

		uname1 = request.POST.get('uname')
		print uname1
		mobile1 = request.POST.get('mobile')
		print mobile1
		s = Userinfo.objects.get(mobile=mobile1)
		username = s.uname
		if(username == uname1):
			# return HttpResponse("welcome")

			return render(request,"snippets/welcome1.html")
		else:
			return HttpResponse("you should login first")

	return render(request,"snippets/login.html")



def resend_otp(request,temp_id):
	print "resend otp"
	qn = Mobile.objects.filter(temp__id=temp_id)
	g = [p.temp_id for p in qn]
	my_id = g[0]


	acti_time = datetime.today() + timedelta(minutes = 30)
	print acti_time
	q = Temp.objects.get(pk = temp_id)
	
	ob_mobile = Mobile()
	# activate_mobile.myuser = myuser
	ob_mobile.otp = random.randint(100000,999999)
	print ob_mobile.otp
	ob_mobile.valid_till = acti_time

	ob_mobile.temp = q
	
	ob_mobile.save()
	return render(request,"snippets/otp.html",{"my_id":my_id} )






# Create your views here.
