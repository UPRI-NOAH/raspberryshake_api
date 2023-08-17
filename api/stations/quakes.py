import requests
from datetime import date, timedelta
from api.stations.models import RaspberryShakeQuakes
from django.contrib.gis.geos import Point

def fetch_quakes():
    quake_url = r'https://quakelink.raspberryshake.org/events/query'
    end_date = date.today()
    start_date = end_date  - timedelta(days=30)
    print(start_date, end_date)
    params = {
        'minlat': 3.951,
        'maxlat': 21.453,
        'minlon': 115.928,
        'maxlon': 127.529,
    }
    quake_response = requests.get(quake_url, params = params)
    if quake_response.status_code ==200:
        # Data format: ${TIMESTAMP};${OTIME};${MAG};${MAG_T};${LAT};${LON};${DEPTH};${PHASES};${AGENCY};${STATUS};${TYPE};${REGION}
        for item in quake_response.text.split('\r\n')[:-1]:
            data = item.split(';')
            obj, created = RaspberryShakeQuakes.objects.get_or_create(code=data[0], defaults={
                'timestamp' : data[1],
                'mag' : data[3],
                'depth' : data[7],
                'agency' : data[9],
                'location' : data[12],
                'loc_pnt' : Point(y = float(data[5]), x = float(data[6])),
            })

if __name__ == '__main__':
    fetch_quakes()