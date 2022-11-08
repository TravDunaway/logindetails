import csv
from pprint import pprint

class Location:

   def __init__(
      self,
      location_id,
      location_type,
      image_url,
      address,
      
   ):
      self.location_id = location_id
      self.location_type = location_type
      self.image_url = image_url
      self.address = address

    def __repr__(self):
        return f"<Location: {self.location_id}, {self.location_type}, {self.address}>"

    def location_types(self):
        return f"${self.location_type}"
    def location_ids(self):
        return f"${self.location_id}"
    def location_address(self):
        return f"{self.address}"

location_dict = {}

with open("locations.csv") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        location_id = row["location_id"]
        
        location = Location(location_id, row["location_type"], row["image_url"], row["address"],)

        location_dict[location_id] = location


pprint(location_dict)


def get_id(location_id):
   return location_dict[location_id]

pprint(get_id("a"))

def get_all():
   return list(location_dict.values())

pprint(get_all())

    