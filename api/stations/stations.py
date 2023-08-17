import requests, datetime
from api.stations.models import RaspberryShakeStations
from django.contrib.gis.geos import Point

def fetch_stations():
    station_url = r'https://api.raspberryshake.org/v1/stations'
    data_url = r'https://stationview.raspberryshake.org/query/objects.json?QC&GM'
    station_response = requests.get(station_url, params = {'net': 'AM'})
    data_response = requests.get(data_url)

    if station_response.status_code ==200 and data_response.status_code ==200:
        station_json = station_response.json()
        data_json = data_response.json()
        data_dict={}
        for item in data_json['request']['GM']['list']:
            code = item['id'][3:]
            data_dict[code] = item
        for st in [x for x in station_json if 'country' in x and x['country']=="Philippines"]:
            station = {}
            for keys in ['code', 'latitude', 'longitude', 'elevation', 'online']:
                station[keys] = st[keys]
            obj, create = RaspberryShakeStations.objects.update_or_create(code=station['code'],defaults= {
                'lat' : station['latitude'],
                'lon' : station['longitude'], 
                'elev' : station['elevation'],
                'online' : station['online'], 
                'acc' : None,
                'vel' : None, 
                'disp' : None, 
                'loc_pnt' : Point(y = station['latitude'], x = station['longitude'])})
            
            if obj.online==True and obj.code in data_dict:
                obj.acc = data_dict[obj.code]['acc']
                obj.vel = data_dict[obj.code]['vel']
                obj.disp = data_dict[obj.code]['disp']
                timestamp = datetime.datetime.utcfromtimestamp(data_dict[obj.code]['timestamp']/1000)
                obj.timestamp = timestamp
                obj.save()

if __name__ == '__main__':
    fetch_stations()