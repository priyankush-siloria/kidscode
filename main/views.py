from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse, HttpResponseRedirect
import pytz
import datetime

from django.template.loader import get_template
from .models import *
from .awsmail import *
import json
# Create your views here.


class HomePage(TemplateView):
	template_name = 'index.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name,{})

class DayPreferences(View):
	def get(self, request, *args, **kwargs):
		response = {}
		zone = request.GET.get("zone")
		day = request.GET.get("day")
		zones = Zones.objects.get(timezone=zone)

		if day != "sun" and day != "sat":
			schedule = zones.others
			day_list = schedule.split(",")

		elif day == "sun":
			schedule = zones.sun
			day_list = schedule.split(",")

		else:
			schedule = zones.sat
			day_list = schedule.split(",")

		response["days"] = day_list
		return HttpResponse(json.dumps(response),content_type='application/json')




class SchedulePage(TemplateView):
	template_name = 'schedule-page.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name,{})

	def post(self, request, *args, **kwargs):
		# track = request.POST.get("track")
		timezone = request.POST.get("zone")
		grade = request.POST.get("grade")
		parentemail = request.POST.get("parentemail")
		phone = request.POST.get("phone")
		if not phone:
			phone = ""
		day1 = request.POST.get("done")
		day2 = request.POST.get("dtwo")
		time1 = request.POST.get("tone")
		time2 = request.POST.get("ttwo")
		if int(grade) < 7:
			track = "Scratch"
		else:
			track = "Python"
		studentname = "Not Available"
		slotaday = ""
		slota = ""
		slotavalue = False
		slotbday = ""
		slotb = ""
		slotbvalue = False
		day_dict = {
		"sun":"Sunday",
		"mon":"Monday",
		"tue":"Tuesday",
		"web":"Wednesday",
		"thu":"Thursday",
		"fri":"Friday",
		"sat":"Saturday"
		}
		slotaday = day_dict[day1]
		slotbday = day_dict[day2]
		contact = request.POST.get("contact")
		if contact:
			contact = True
		else:
			contact = False

		slopta_split= time1.split("-")
		sloptb_split= time2.split("-")
		if timezone=="pst":
			timezonevaluez = "US/Pacific"
		if timezone=="ist":
			timezonevaluez = "Asia/Kolkata"
		if timezone=="est":
			timezonevaluez = "US/Eastern"
		if timezone=="cst":
			timezonevaluez = "US/Central"
		if timezone=="mst":
			timezonevaluez = "US/Mountain"
		pstslota = []
		pstslotb = []
		istslota = []
		istslotb = []
		for slot1 in slopta_split:
			datetime_object = datetime.datetime.strptime(slot1, '%I:%M %p')
			datetime_obj = datetime_object.replace(tzinfo=pytz.timezone(timezonevaluez))

			pst_timezone = pytz.timezone("US/Pacific")
			ist_timezone = pytz.timezone("Asia/Kolkata")

			my_timestamp_in_pst_timezone = datetime_obj.astimezone(pst_timezone)
			my_timestamp_in_ist_timezone = datetime_obj.astimezone(ist_timezone)

			pstslota.append(my_timestamp_in_pst_timezone.strftime("%I:%M %p"))
			istslota.append(my_timestamp_in_ist_timezone.strftime("%I:%M %p"))

		for slot2 in sloptb_split:
			datetime_object = datetime.datetime.strptime(slot2, '%I:%M %p')
			datetime_obj = datetime_object.replace(tzinfo=pytz.timezone(timezonevaluez))

			pst_timezone = pytz.timezone("US/Pacific")
			ist_timezone = pytz.timezone("Asia/Kolkata")

			my_timestamp_in_pst_timezone = datetime_obj.astimezone(pst_timezone)
			my_timestamp_in_ist_timezone = datetime_obj.astimezone(ist_timezone)

			pstslotb.append(my_timestamp_in_pst_timezone.strftime("%I:%M %p"))
			istslotb.append(my_timestamp_in_ist_timezone.strftime("%I:%M %p"))


		Schedule.objects.create(
				track=track,
				grade=grade,
				timezone=timezone,
				slotaday=slotaday,
				slota=time1,
				slotbday=slotbday,
				slotb=time2,
				stuname=studentname,
				pemail=parentemail,
				phone=phone,
				pstslota="-".join(pstslota),
				istslota="-".join(istslota),
				pstslotb="-".join(pstslotb),
				istslotb="-".join(istslotb),
				contact=contact
			)
		template = get_template("scheduleapplication.html")
		c = {
			'track': track,
			'timezone': timezone,
			'stuname': studentname,
			'pemail' : parentemail,
			'slotaday' : slotaday,
			'slota' : slota,
			'slotbday' : slotbday,
			'slotb' : slotb
		}
		mail_content = template.render(c)
		# recipientlist = ["learn@skoolofcode.com","shivprashant@gmail.com"]
		recipientlist = ["rajindermohan001@gmail.com"]
		subject = "New Schedule Application Submission"
		awsMailSending(recipientlist,subject,mail_content)
		return HttpResponseRedirect('schedule?result=success')

