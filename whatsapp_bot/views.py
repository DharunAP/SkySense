from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Profile
from geopy.geocoders import Nominatim
import requests
import json
import geocoder




alert = [
    {
        'warning': 'thunderstorm with heavy rain',
        'id':'202',
        'message': """Attention Please!
        🌩 Skysense Weather Update 🌧

                Hello there! This is Skysense, your trusted weather companion. Here's your weather forecast for today:

                Location: Coimbatore
                Date: 16/7/23

                🌡 Temperature: {temperature}
                ☁ Weather Condition: {description}
                💨 Wind Speed: {wind}
                💦 Humidity: {humidity}

                🚨 Today's Weather Alert:

                ⚠ Severe Thunderstorm Warning ⚠

                A thunderstorm with heavy rain is approaching Coimbatore. Take immediate precautions to ensure your safety.
                🌧 Weather Impact:

                ⿡ Heavy Rainfall: Expect intense downpour with the potential for localized flooding. Be vigilant around low-lying areas and avoid crossing flooded roads.

                ⿢ Thunder and Lightning: Anticipate frequent thunder and lightning activity. Stay indoors and avoid open areas to reduce the risk of lightning strikes.

                ⿣ Strong Winds: Prepare for gusty winds that may result in fallen branches or flying debris. Secure loose objects to prevent damage or injury.

                ⿤ Reduced Visibility: Exercise caution while driving or traveling due to decreased visibility caused by heavy rain and thunderstorm activity.

                📝 Safety Tips:

                ⿡ Seek Shelter: Move indoors to a safe location, preferably a sturdy building or a designated storm shelter. Stay away from windows and doors.

                ⿢ Stay Informed: Stay updated with the latest weather updates from reliable sources. Follow instructions and warnings issued by local authorities.

                ⿣ Emergency Preparedness: Have essential supplies like flashlights, batteries, non-perishable food, and a first aid kit readily available.

                ⿤ Postpone Outdoor Activities: Avoid outdoor activities until the thunderstorm subsides and conditions improve.

                Please stay safe and take necessary precautions during this thunderstorm with heavy rain. If you have any further inquiries, feel free to reach out. Take care! ⛈😊

                Skysense Weather Team





                """,
    },
    {
        'warning': 'heavy thunderstorm',
        'id':'212',
        'message': """
                Attention Please!
                🌩 Skysense Weather Update 🌩

                Hello there! This is Skysense, your trusted weather companion. Here's your weather forecast for today:

                Location: Coimbatore
                Date: 16/7/23

                🌡 Temperature: {temperature}
                    ☁ Weather Condition: {description}
                    💨 Wind Speed: {wind}
                    💦 Humidity: {humidity}

                🚨 Today's Weather Alert:

                ⚠ Severe Thunderstorm Warning ⚠

                A heavy thunderstorm is approaching Coimbatore, bringing potential hazards. Take immediate precautions to ensure your safety.
                🌧 Weather Impact:

                ⿡ Intense Rainfall: Expect heavy downpour and localized flooding. Be cautious of water accumulation and potential flash floods.

                ⿢ Strong Winds: Prepare for gusty winds and take measures to secure loose objects to prevent damage or injury.

                ⿣ Lightning Strikes: Seek shelter indoors and avoid open areas to reduce the risk of lightning strikes.

                ⿤ Reduced Visibility: Exercise caution while driving or traveling due to limited visibility caused by heavy rain and thunderstorm activity.

                📝 Safety Tips:

                ⿡ Seek Shelter: Move indoors to a safe location, preferably a sturdy building or a designated storm shelter. Stay away from windows and doors.

                ⿢ Stay Informed: Keep updated with the latest weather updates from reliable sources. Follow instructions from local authorities.

                ⿣ Emergency Preparedness: Have essential supplies like flashlights, batteries, non-perishable food, and a first aid kit on hand.

                ⿤ Postpone Outdoor Activities: Avoid venturing outside until the storm passes and conditions improve.

                Please stay safe and take necessary precautions during this heavy thunderstorm. Feel free to reach out if you have any further inquiries. Take care! ⛈😊

                Skysense Weather Team""",
    },
    {
        'warning': 'thunderstorm with heavy drizzle',
        'id':'232',
        'message': """
                        Greeting! This is Skysense, your weather companion bot. Here's your daily weather forecast for today:

                            Location: Coimbatore
                            Date: 16/7/23

                            🌡 Temperature: {temperature}
                            ☁ Weather Condition: {description}
                            💨 Wind Speed: {wind}
                            💦 Humidity: {humidity}

                            📝 Today's Weather Advisories:

                            ⚠ Severe Weather Alert: A thunderstorm with heavy drizzle is expected in Coimbatore. Take the following precautions:

                            ⿡ Seek shelter: Find a safe location indoors, away from windows and exterior walls.

                            ⿢ Stay informed: Keep updated on the latest weather reports and follow any instructions from local authorities.

                            ⿣ Be cautious on the roads: Exercise caution while driving due to reduced visibility and potentially slippery conditions.

                            ⿤ Secure outdoor objects: Safely secure or bring indoors any items that could be affected by strong winds.

                            ⿥ Avoid flooded areas: Stay away from flooded roads, bridges, and low-lying areas. Do not attempt to cross flowing water.

                            Stay safe and dry during the thunderstorm with heavy drizzle. If you have any questions or need further assistance, feel free to ask. Take care! ☔😊

                            Skysense Weather Team





                            Regenerate response
                    """,
    },
    {
        'warning': 'heavy intensity drizzle',
        'id':'302',
        'message': """Attention Please!
        ☔ Skysense Weather Update ☁

                Hello! This is Skysense, your trusted weather companion. Here's your weather forecast for today:

                Location: Coimbatore
                Date: 16/7/23

                🌡 Temperature: {temperature}
                ☁ Weather Condition: {description}
                💨 Wind Speed: {wind}
                💦 Humidity: {humidity}

                ⚠ Today's Weather Alert:

                Heavy Intensity Drizzle Warning ⚠
                A heavy intensity drizzle is expected in Coimbatore. While not severe, it's important to stay prepared and take precautions.

                🌧 Weather Impact:

                ⿡ Moderate Rainfall: Anticipate a continuous and steady drizzle with moderate rainfall throughout the day.

                ⿢ Reduced Visibility: Be cautious while driving or commuting due to reduced visibility caused by the heavy intensity drizzle.

                ⿣ Slippery Conditions: Watch out for slippery surfaces, such as roads, walkways, and stairs. Take necessary precautions to prevent accidents.

                📝 Safety Tips:

                ⿡ Carry an Umbrella: Keep an umbrella or raincoat handy to stay dry during the heavy drizzle.

                ⿢ Wear Proper Footwear: Opt for non-slip shoes or boots to maintain better traction on wet surfaces.

                ⿣ Drive Safely: Slow down and maintain a safe distance from other vehicles. Turn on your headlights and use caution while braking.

                ⿤ Stay Dry: Wear appropriate rain gear and protect electronic devices from moisture.

                Please stay cautious and take necessary measures during this period of heavy intensity drizzle. If you have any further inquiries, feel free to reach out. Stay safe! ☔😊

                Skysense Weather Team""",
    },
    {
        'warning': 'heavy intensity drizzle rain',
        'id':'312',
                    'message': """Attention Please!
                    ☔ Skysense Weather Update ☁

            Hello! This is Skysense, your trusted weather companion. Here's your weather forecast for today:

            Location: Coimbatore
            Date: 16/7/23

            🌡 Temperature: {temperature}
                ☁ Weather Condition: {description}
                💨 Wind Speed: {wind}
                💦 Humidity: {humidity}

            ⚠ Today's Weather Alert:

            Heavy Intensity Drizzle with Rain Warning ⚠
            Coimbatore is experiencing heavy intensity drizzle with rain. Please take necessary precautions to ensure your safety.

            🌧 Weather Impact:

            ⿡ Heavy Intensity Drizzle: Expect continuous and heavy drizzle combined with rainfall throughout the day.

            ⿢ Reduced Visibility: Exercise caution while driving or commuting due to reduced visibility caused by the heavy intensity drizzle and rain.

            ⿣ Slippery Conditions: Be mindful of slippery surfaces, such as roads, walkways, and stairs. Take necessary precautions to prevent accidents.

            📝 Safety Tips:

            ⿡ Carry an Umbrella: Keep an umbrella or raincoat handy to stay dry during the heavy intensity drizzle and rain.

            ⿢ Wear Proper Footwear: Opt for non-slip shoes or boots to maintain better traction on wet surfaces.

            ⿣ Drive Safely: Slow down and maintain a safe distance from other vehicles. Turn on your headlights and use caution while braking.

            ⿤ Stay Dry: Wear appropriate rain gear and protect electronic devices from moisture.

            Please stay cautious and take necessary measures during this period of heavy intensity drizzle with rain. If you have any further inquiries, feel free to reach out. Stay safe! ☔😊

            Skysense Weather Team""",
    },
    {
        'warning': 'heavy intensity rain',
        'id':'502',
                    'message': """Attention Please!
                    ☔ Skysense Weather Update ☔

            Hello! This is Skysense, your trusted weather companion. Here's your weather forecast for today:

            Location: Coimbatore
            Date: 16/7/23

            🌡 Temperature: {temperature}
                ☁ Weather Condition: {description}
                💨 Wind Speed: {wind}
                💦 Humidity: {humidity}

            ⚠ Today's Weather Alert:

            Heavy Intensity Rain Warning ⚠
            Coimbatore is currently experiencing heavy intensity rain. Please take necessary precautions to ensure your safety.

            🌧 Weather Impact:

            ⿡ Heavy Intensity Rainfall: Expect continuous and heavy rainfall throughout the day.

            ⿢ Possible Flooding: Be cautious of potential flooding in low-lying areas and near water bodies. Avoid crossing flooded roads.

            ⿣ Reduced Visibility: Exercise caution while driving or commuting due to reduced visibility caused by the heavy intensity rain.

            📝 Safety Tips:

            ⿡ Stay Indoors: If possible, remain indoors until the heavy rain subsides. Seek shelter in a safe and dry location.

            ⿢ Monitor Water Levels: Stay informed about any flood warnings or advisories issued by local authorities.

            ⿣ Avoid Flooded Areas: Do not attempt to walk, drive, or swim through flooded areas. Turn around and find an alternate route.

            ⿤ Stay Connected: Keep your mobile devices charged and stay updated with weather alerts and updates from reliable sources.

            Please stay cautious and take necessary measures during this period of heavy intensity rain. If you have any further inquiries, feel free to reach out. Stay safe! ☔😊

            Skysense Weather Team""",
    },
    {
        'warning': 'extreme rain',
        'id':'504',
                        'message': """Attention Please!
                        ☔ Skysense Weather Update ☔

                Hello! This is Skysense, your trusted weather companion. Here's your weather forecast for today:

                Location: Coimbatore
                Date: 16/7/23

                🌡 Temperature: {temperature}
                ☁ Weather Condition: {description}
                💨 Wind Speed: {wind}
                💦 Humidity: {humidity}

                ⚠ Today's Weather Alert:

                Extreme Rain Warning ⚠
                Coimbatore is currently experiencing extreme rainfall. Please take immediate precautions to ensure your safety.

                🌧 Weather Impact:

                ⿡ Extreme Rainfall: Expect intense and prolonged rainfall throughout the day, potentially leading to widespread flooding.

                ⿢ Flash Floods: Be aware of the possibility of flash floods in low-lying areas and near water bodies. Avoid crossing flooded roads.

                ⿣ Limited Visibility: Exercise extreme caution while driving or commuting due to significantly reduced visibility caused by the heavy rain.

                📝 Safety Tips:

                ⿡ Stay Indoors: It is strongly advised to stay indoors and avoid unnecessary travel during extreme rain conditions.

                ⿢ Emergency Preparedness: Have essential supplies, such as food, water, flashlights, and a first aid kit, readily available.

                ⿣ Monitor Updates: Stay tuned to local weather reports and emergency notifications for the latest information and guidance.

                ⿤ Follow Authorities' Instructions: Adhere to any evacuation orders or safety directives issued by local authorities.

                Please prioritize your safety and take immediate measures during this period of extreme rain. If you have any further inquiries, feel free to reach out. Stay safe! ☔😊

                Skysense Weather Team""",
    },
    {
        'warning': 'freezing rain',
        'id':'511',
        'message': """
                Attention Please!
                ❄ Skysense Weather Update ❄

                Hello! This is Skysense, your trusted weather companion. Here's your weather forecast for today:

                Location: Coimbatore
                Date: 16/7/23

                🌡 Temperature: {temperature}
                    ☁ Weather Condition: {description}
                    💨 Wind Speed: {wind}
                    💦 Humidity: {humidity}

                ⚠ Today's Weather Alert:

                Freezing Rain Warning ⚠
                Coimbatore is currently experiencing freezing rain. Please take immediate precautions as this can create hazardous conditions.

                ❄ Weather Impact:

                ⿡ Freezing Rain: Expect rain that freezes upon contact with the ground or surfaces, forming a layer of ice.

                ⿢ Hazardous Road Conditions: Be cautious of icy roadways, sidewalks, and other surfaces. They can be extremely slippery.

                ⿣ Power Outages: Freezing rain can cause ice accumulation on power lines, potentially leading to power outages.

                📝 Safety Tips:

                ⿡ Stay Indoors: If possible, remain indoors and avoid travel until conditions improve.

                ⿢ Use Caution: If you must go outside, walk slowly and carefully on icy surfaces. Use handrails for support.

                ⿣ Dress Warmly: Wear warm clothing and appropriate footwear to stay comfortable in cold temperatures.

                ⿤ Be Prepared: Have emergency supplies, such as flashlights, batteries, non-perishable food, and blankets, readily available.

                Please prioritize your safety and take immediate measures during freezing rain conditions. If you have any further inquiries, feel free to reach out. Stay safe! ❄😊

                Skysense Weather Team""",
    },
    {
        'warning': 'heavy intensity shower rain',
        'id':'522',
                        'message': """Attention Please!
                        ☔ Skysense Weather Update ☔

                Hello! This is Skysense, your trusted weather companion. Here's your weather forecast for today:

                Location: Coimbatore
                Date: 16/7/23

                🌡 Temperature: {temperature}
                    ☁ Weather Condition: {description}
                    💨 Wind Speed: {wind}
                    💦 Humidity: {humidity}

                ⚠ Today's Weather Alert:

                - Heavy Intensity Shower Rain Warning ⚠

                Coimbatore is currently experiencing heavy intensity shower rain. Please take necessary precautions as this may cause localized impacts.

                🌧 Weather Impact:

                ⿡ Heavy Intensity Rainfall: Expect intense and heavy showers with increased rainfall rates for a limited period of time.

                ⿢ Rapid Accumulation: Be cautious of rapid water accumulation in low-lying areas and potential localized flooding.

                ⿣ Reduced Visibility: Exercise caution while driving or commuting due to reduced visibility caused by heavy shower rain.

                📝 Safety Tips:

                ⿡ Carry an Umbrella or Raincoat: Keep an umbrella or raincoat handy to stay dry during the heavy intensity shower rain.

                ⿢ Watch for Flooded Areas: Be mindful of potential flooding in low-lying areas and near water bodies. Avoid crossing flooded roads.

                ⿣ Drive Safely: Reduce speed and maintain a safe distance from other vehicles. Turn on your headlights and use caution while braking.

                ⿤ Stay Dry Indoors: If possible, stay indoors until the heavy shower rain subsides to minimize exposure to wet conditions.

                Please stay cautious and take necessary measures during this period of heavy intensity shower rain. If you have any further inquiries, feel free to reach out. Stay safe! ☔😊

                Skysense Weather Team""",
    },
    {
        'warning': 'heavy snow',
        'id':'602',
                        'message':"""Attention Please!
                        ❄ Skysense Weather Update ❄

                Hello! This is Skysense, your trusted weather companion. Here's your weather forecast for today:

                Location: Coimbatore
                Date: 16/7/23

                🌡 Temperature: {temperature}
                    ☁ Weather Condition: {description}
                    💨 Wind Speed: {wind}
                    💦 Humidity: {humidity}

                ⚠ Today's Weather Alert:

                - Heavy Snowfall Warning ⚠

                Coimbatore is currently experiencing heavy snowfall. Please take immediate precautions as this can create challenging conditions.

                ❄ Weather Impact:

                ⿡ Heavy Snowfall: Expect intense and continuous snowfall, leading to significant snow accumulation.

                ⿢ Reduced Visibility: Exercise extreme caution while driving or commuting due to reduced visibility caused by heavy snow.

                ⿣ Hazardous Road Conditions: Be aware of slippery and icy roadways. Travel may be difficult or dangerous.

                📝 Safety Tips:

                ⿡ Stay Indoors: If possible, remain indoors and avoid unnecessary travel until conditions improve.

                ⿢ Dress Warmly: Layer up with warm clothing, including hats, gloves, scarves, and insulated footwear.

                ⿣ Clear Pathways: Safely remove snow from driveways, walkways, and stairs to prevent slips and falls.

                ⿤ Use Caution: If you must go outside, walk slowly and carefully on snowy or icy surfaces. Use handrails for support.

                Please prioritize your safety and take immediate measures during heavy snowfall conditions. If you have any further inquiries, feel free to reach out. Stay safe and warm! ❄😊

                Skysense Weather Team""",
    },
    {
        'warning': 'heavy shower snow',
        'id':'622',
                        'message': """Attention Please!
                        ❄ Skysense Weather Update ☔

                Hello! This is Skysense, your trusted weather companion. Here's your weather forecast for today:

                Location: Coimbatore
                Date: 16/7/23

                🌡  Temperature: {temperature}
                    ☁ Weather Condition: {description}
                    💨 Wind Speed: {wind}
                    💦 Humidity: {humidity}
                ⚠ Today's Weather Alert:

                - Heavy Shower Snow Warning ⚠

                Coimbatore is currently experiencing heavy shower snow. Please take necessary precautions as this may cause localized impacts.

                ❄ Weather Impact:

                ⿡ Heavy Snowfall: Expect intense and heavy snow showers for a limited period of time.

                ⿢ Rapid Snow Accumulation: Be cautious of rapid snow accumulation, which may lead to slippery surfaces and reduced visibility.

                ⿣ Hazardous Road Conditions: Drive with caution and be aware of slippery and icy roadways.

                📝 Safety Tips:

                ⿡ Dress Warmly: Layer up with warm clothing, including hats, gloves, scarves, and insulated footwear.

                ⿢ Use Caution: If you must go outside, walk slowly and carefully on snowy or icy surfaces. Use handrails for support.

                ⿣ Clear Pathways: Safely remove snow from driveways, walkways, and stairs to prevent slips and falls.

                ⿤ Drive Safely: Reduce speed and maintain a safe distance from other vehicles. Use winter tires or chains if necessary.

                Please stay cautious and take necessary measures during this period of heavy shower snow. If you have any further inquiries, feel free to reach out. Stay safe and warm! ❄😊

                Skysense Weather Team""",
    },
    {
        'warning': 'tornado',
        'id':'781',
        'message': """Attention Please!
        🌪 Skysense Weather Update 🌪

        Hello! This is Skysense, your trusted weather companion. Here's your weather alert for today:

        Location: Coimbatore
        Date: 16/7/23

        🌡 Temperature: {temperature}
        ☁ Weather Condition: {description}
        💨 Wind Speed: {wind}
        💦 Humidity: {humidity}

        ⚠ Today's Weather Alert:

        - Tornado Warning ⚠

        Coimbatore is currently under a tornado alert. Please take immediate precautions as this is a dangerous weather situation.

        🌪 Weather Impact:

        ⿡ Tornado Formation: A tornado is expected to form in the area, bringing strong and destructive winds.

        ⿢ High Wind Speeds: Expect rapidly increasing wind speeds, with gusts potentially exceeding 100 km/h.

        ⿣ Structural Damage: Tornadoes can cause significant damage to buildings, trees, and infrastructure.

        ⿤ Flying Debris: Take caution against flying debris, which can pose a serious risk to personal safety.

        📝 Safety Tips:

        ⿡ Seek Shelter: Move immediately to a sturdy and secure location, preferably an underground shelter or an interior room without windows.

        ⿢ Stay Informed: Keep updated with the latest weather information through local news, radio, or weather alert systems.

        ⿣ Follow Authorities' Instructions: Adhere to any evacuation orders or safety directives issued by local authorities.

        ⿤ Stay Away from Windows: Protect yourself from broken glass and flying debris by staying away from windows and exterior walls.

        ⿥ Remain Calm: Stay calm and reassure others, especially children and pets, while taking necessary precautions.

        Please prioritize your safety and take immediate measures during this tornado alert. If you have any further inquiries, feel free to reach out. Stay safe! 🌪😊

        Skysense Weather Team""",
    },

]




def lati(landmark):
    # Create a geocoder object
    geolocator = Nominatim(user_agent="my_app")

    # Get the landmark input from the user

    # Perform geocoding to retrieve the latitude and longitude
    location = geolocator.geocode(landmark)

    # Check if a valid location was found
    if location is not None:
        latitude = location.latitude
        longitude = location.longitude
        return latitude,longitude
    else:
        return None,None

def datas(x):
   
    l=Profile.objects.get(user_id=x)
    latitude = l.latitude # g.latlng[0]
    longitude = l.longitude # g.latlng[1]

    # Usage

    # Set the API endpoint URL

    url = "https://api.openweathermap.org/data/2.5/weather"
    next_5days = "https://api.openweathermap.org/data/2.5/forecast"

    # Set the parameters, including your API key and location

    appid = "51f23d19d99ec7e1584ccda0e50ef6ad"
    next_5days += f'?lat={latitude}&lon={longitude}&appid={appid}'

    # Make the HTTP GET request
    response = requests.get(next_5days)

    # Parse the JSON response
    data = response.json()


    weather_list = data['list']


    weather_id = []
    past_date = []
    i =0
    for day in weather_list:
        date = day['dt_txt'].split()
        first_word = date[0]

        if first_word not in past_date:
            past_date.append(first_word)

            li = {
                'temp':day['main']['temp'],
                'humidity':day['main']['humidity'],
                'date':day['dt_txt'],
                'id':day['weather'][0]['id'],
                'main':day['weather'][0]['main'],
                'description':day['weather'][0]['description'],
                'temp_min':day['main']['temp_min'],
                'temp_max':day['main']['temp_max'],
                'location':l.landmark.capitalize()
            }
            print(li['main'])
            print('des',li['description'])
            weather_id.append(li)
        

    return weather_id

def alerts(first):
    print(first)
    climate_id = first['id']
    print('cid ::',climate_id)
    fl = 0
    for climate in alert:
        if str(climate_id) in climate['id']:
            message = climate['message']
            message = message.format(temperature=first['temp'],description=first['description'],wind=50,humidity=first['humidity'])
            print(message)
            fl = 1
    final_temp = int(((first['temp_min']+first['temp_max'])-2*273)//2)
    mes="""
\tCondition: {main}
\tDescription: {description}! 
\tTemperature: {final_temp}°C
\tHumidity: {humidity}%
""".format(final_temp=final_temp,temp_min=first['temp_min'],temp_max=first['temp_max'],description=first['description'].capitalize(),humidity=first['humidity'],main=first['main'])
    return mes


def home(request):
    first={'id':None,'main':None,'temp':None,'location':None}
    next_four=None
    if request.user.is_authenticated:
        climate_data = datas(request.user.id)
        first = climate_data[0]
        print(first)
        alerts(first)
        second =climate_data[1]
        third =climate_data[2]
        froth = climate_data[3]
        fifth = climate_data[4]
        next_four =[[second['id'],second['main'],'Day - 2'],[third['id'],third['main'],'Day -3'],[froth['id'],froth['main'],'Day - 4'],[fifth['id'],fifth['main'],'Day - 5']]
        print(next_four)
        first['temp']=int(first['temp']-273)
    return render(request,'home.html',{
        'first_id':first['id'],
        'first_main':first['main'],
        'land':first['location'],
        'temp':first['temp'],
        'next_four':next_four,
    })


def signup(request):
    us=list(User.objects.all().values_list('username',flat=True))
    if request.method=='POST':
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        city=request.POST.get('inputdistrict')
        state=request.POST.get('inputstate')
        sms=bool(request.POST.get('sms'))
        password1=request.POST.get('pass1')
        password2=request.POST.get('pass2')
        land=request.POST.get('land')
        lat,lon=lati(land)
        if len(phone)!=10 or not phone.isdigit():
            messages.error('Enter a valid phone number of 10 digits...')
        elif username not in us and password1==password2 and lat and lon and len(str(phone))==10:
            x=User.objects.create(
                username=username,
                password=password1,
            )
            Profile.objects.create(
                user=x,
                phone_no=phone,
                city=city,
                state=state,
                sms_enabled=sms,
                landmark=land,
                latitude=lat,
                longitude=lon,
            )
            login(request,x)
            return redirect('whatsapp_permission')
        elif lat==None and lon==None:
            messages.error(request,'Couldn\'t find the location. Try giving any city names...')
        elif username in us:
            messages.error(request,'Username already exits...')
        elif password1!=password2:
            messages.error(request,'Passwords doesn\'t match...')
        else:
            messages.error(request,'Enter a valid phone number')
        print(messages,'hi')
        
    return render(request, 'signup.html')

def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            #messages="User doesn't exist."
            messages.error(request, 'User doesn\'t exist')
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user )
            return redirect('home')
        else:
            messages.error(request,'Username or password doesn\'t match...')
        

    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('home')

def whatsapp_permission(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method=='POST':
        climate_data = datas(request.user.id)
        first = climate_data[0]
        mes=alerts(first[0])
        profile=Profile.objects.get(user_id=request.user.id)

        # from twilio.rest import Client

        account_sid = 'ACab0736136e82a45256bdb3e56ee9a20d'
        auth_token = '3fa3dd0f864aeaeead60737316c6f423'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="""Hello! This is Sky Sense, your trusted weather companion.\n🌤️ Weather Forecast for Today - {} 🌤️""".format(str(profile.landmark))+str(mes),
        to='whatsapp:+91'+str(profile.phone_no)
        )
        return redirect('home')
    return render(request,'whatsapp.html')
