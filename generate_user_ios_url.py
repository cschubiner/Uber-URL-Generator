import urllib

# uber://?client_id=YOUR_CLIENT_ID&action=setPickup&pickup[latitude]=37.800071&pickup[longitude]=-122.432009&pickup[nickname]=1857LombardSt&pickup[formatted_address]=1857+Lombard+Street+San+Francisco+94123&dropoff[latitude]=37.802374&dropoff[longitude]=-122.405818&dropoff[nickname]=Airbnb%20HQ&dropoff[formatted_address]=1%20Telegraph%20Hill%20Blvd%2C%20San%20Francisco%2C%20CA%2094133&product_id=a1111c8c-c720-46c3-8534-2fcdd730040d

def genurl_my_loc(dlat, dlong, dname):
  print
  print 'Uber to',dname
  nickname2 = [dname, dname]
  for key in nDict:
    if key in dname:
      nickname2 = nDict[key]
  return 'uber://?client_id=YOUR_CLIENT_ID&action=setPickup&pickup=my_location&dropoff[latitude]={0}&dropoff[longitude]={1}&dropoff[nickname]={2}&dropoff[formatted_address]={3}&product_id=a1111c8c-c720-46c3-8534-2fcdd730040d'.format(dlat, dlong, formatNickname(nickname2[0]), formatNickname(nickname2[1]))

def formatNickname(s):
  return str(urllib.quote_plus(s)).replace('+','%20')

nDict = {
  '1857':['Death Star', "That's no moon. It's a space station"],
  '202':['Alderaan', 'I feel a great disturbance in the Force...'],
  '888':['The Cupboard under the Stairs', '4 Privet Drive, Little Whinging, Surrey'],
}
def genurl(plat, plong, pname, dlat, dlong, dname):
  print
  nickname1 = [pname, pname]
  nickname2 = [dname, dname]
  for key in nDict:
    if key in pname:
      nickname1 = nDict[key]
    if key in dname:
      nickname2 = nDict[key]

  print pname[:15],'to',dname
  return 'uber://?client_id=YOUR_CLIENT_ID&action=setPickup&pickup[latitude]={0}&pickup[longitude]={1}&pickup[nickname]={2}&pickup[formatted_address]={7}&dropoff[latitude]={3}&dropoff[longitude]={4}&dropoff[nickname]={5}&dropoff[formatted_address]={6}&product_id=a1111c8c-c720-46c3-8534-2fcdd730040d'.format(plat, plong, formatNickname(nickname1[0]), dlat, dlong, formatNickname(nickname2[0]), formatNickname(nickname2[1]), formatNickname(nickname1[1]))

print genurl('37.800071', '-122.432009', '1857 Lombard St. San Francisco 94123', '37.772123',  '-122.405293', '888 Brannan St. San Francisco 94103')

print genurl('37.772123',  '-122.405293', '888 Brannan St. San Francisco 94103', '37.800071', '-122.432009', '1857 Lombard St. San Francisco 94123')

print genurl('37.800071', '-122.432009', '1857 Lombard St. San Francisco 94123', '37.583447',  '-122.341823', '704 Concord Way Burlingame 94010')

print genurl('37.583447',  '-122.341823', '704 Concord Way Burlingame 94010','37.800071', '-122.432009', '1857 Lombard St. San Francisco 94123')

print genurl_my_loc('37.772123',  '-122.405293', '888 Brannan St. San Francisco 94103')

print genurl_my_loc('37.800071', '-122.432009', '1857 Lombard St. San Francisco 94123')

print genurl_my_loc('37.583447',  '-122.341823', '704 Concord Way Burlingame 94010')

print genurl_my_loc('37.769435', '-122.406394', '202 Division St. San Francisco 94103')
print genurl('37.769435', '-122.406394', '202 Division St. San Francisco 94103', '37.800071', '-122.432009', '1857 Lombard St. San Francisco 94123')
