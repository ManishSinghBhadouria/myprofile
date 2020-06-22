from django.shortcuts import render,HttpResponse,redirect
import urllib.request
import socket
from getmac import get_mac_address as gma
from . models import notes
# Create your views here.
def index(request):
    user= notes.objects.get(sname="resume")
    return  render (request,'index.html',{'user':user})


def downloadcv(request):
    return  render (request,'index.html')

def CheckInternet(request):
    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host) #Python 3.x
            return True
        except:
            return False
    if connect():
        return HttpResponse("Connected To Internet")
    return  HttpResponse("Not Connected To Internet")

def MacIp(request): 
    host_name = socket.gethostname() 
    host_ip = socket.gethostbyname(host_name)
    a="Host-Name = " + host_name
    b="   ,   IP Address = " + host_ip
    d="   ,   MAC Address = " + gma() + "MilliSecond"
    c=[a,b,d]
    return HttpResponse(c)

def NetSpeed(request): 
    import speedtest
    st = speedtest.Speedtest()
    an=st.upload()
    bn=st.download()
    dn=st.results.ping
    a="Upload = " + str(an)
    b="   ,   Download = " + str(bn)
    d="   ,   Ping = " + str(dn)
    c=[a,b,d]
    return HttpResponse(c)

    

def IpLoc(request): 
    import geocoder
    g = geocoder.ip('me')
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(g.latlng, exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')

    a="City = " + str(city)
    b="   ,   State = " + str(state)
    d="   ,   Country = " + str(country)
    c=[a,b,d]
    return HttpResponse(c)


def PinLoc(request): 
    if request.method == 'POST':
        pincode = request.POST['pincode']
        from geopy.geocoders import Nominatim
        geolocator = Nominatim(user_agent="geoapiExercises")
        zipcode1 = pincode
        print("\nZipcode:",zipcode1)
        location = geolocator.geocode(zipcode1)
        print("Details of the said pincode:")
        print(location.address)
    return HttpResponse(location.address)


def Utube(request):
    import pafy
    if request.method == 'POST':
        url = request.POST['url']
        what = request.POST['gender']
        result = pafy.new(url)
        if what=="video":
            best_quality_video = result.getbest()
            best_quality_video.download()  #best_quality_video.download(filepath="/home/mihir/PycharmProjects/web_crawlers/")
        elif what=="audio":
            best_quality_audio = result.getbestaudio()
            best_quality_audio.download()
        else:
            best_quality_video = result.getbest()
            best_quality_video.download()
            best_quality_audio = result.getbestaudio()
            best_quality_audio.download()
    return redirect(index)


def UtubeDesc(request):
    import pafy
    if request.method == 'POST':
        url = request.POST['url']
        result = pafy.new(url)
        ## getting details like title, rating, viewcount, author, length, likes, etc..,
        Title = "Title Of Video = " + str(result.title)
        Viewcount = ", Total View = " + str(result.viewcount)
        Author = ", Author = " + str(result.author)
        Video_Length = ", Video_Length = " + str(result.length)
        Likes = ", Likes = " + str(result.likes)
        Dislikes = ", DisLikes = " + str(result.dislikes)
        Duration = ", Duration = " + str(result.duration)
        Rating = ", Rating = " + str(result.rating)
        detail=[Title,Viewcount,Author,Video_Length,Likes,Dislikes,Duration,Rating]
    return HttpResponse(detail)


