from json import dumps

from apps.dispatch.models import RecievedReciept


def extract_lat_long_via_address():
    LocationsForMap = []
    each_property = []
    for property in RecievedReciept.objects.all():
        if property.latitude and property.longitude:
            each_property.append(property.state.name)
            each_property.append(float(property.latitude))
            each_property.append(float(property.longitude))
            LocationsForMap.append(each_property)
            each_property = []
    dataJSON = dumps(LocationsForMap)
    return dataJSON
