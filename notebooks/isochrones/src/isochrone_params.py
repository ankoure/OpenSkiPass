import math


class Isochrone_params:
    def __init__(self, max_time, interval, lon, lat):
        # interval and max time in minutes
        self.max_time = max_time
        self.interval = interval
        self.lon = lon
        self.lat = lat
        self.id = (
            "valhalla_isochrones_lonlat_"
            + str(lon)
            + ","
            + str(lat)
            + str(max_time)
            + "_interval_"
            + str(interval)
        )

    def generatecontours(self):
        # array to nest arrays in
        chunks = []
        time_counter = 0

        iterations = math.ceil((self.max_time / self.interval) / 4)
        current_iteration = 1
        while current_iteration <= iterations:
            # set local counter
            i = 0
            # local chunk consisting of no more than 4 interval times
            chunk = []
            while i < 4:
                i += 1
                time_counter += self.interval
                if time_counter < self.max_time:
                    chunk.append(time_counter)
                else:
                    if self.max_time not in chunk:
                        # make sure final time only gets added once
                        chunk.append(time_counter)
                    else:
                        pass
                        # do nothing as max time is already in chunk

            chunks.append(chunk)
            current_iteration += 1
        # returns nested list of intervals dicts
        return chunks

    def create_isochrone_request(self, contour_times):
        return {
            "polygons": True,
            "denoise": "0.1",
            "generalize": "0",
            "show_locations": True,
            "costing": "auto",
            "costing_options": {
                "auto": {
                    "maneuver_penalty": 5,
                    "country_crossing_penalty": 0,
                    "country_crossing_cost": 600,
                    "width": 1.6,
                    "height": 1.9,
                    "use_highways": 1,
                    "use_tolls": 1,
                    "use_ferry": 1,
                    "ferry_cost": 300,
                    "use_living_streets": 0.5,
                    "use_tracks": 0,
                    "private_access_penalty": 450,
                    "ignore_closures": False,
                    "ignore_restrictions": False,
                    "ignore_access": False,
                    "closure_factor": 9,
                    "service_penalty": 15,
                    "service_factor": 1,
                    "exclude_unpaved": 1,
                    "shortest": False,
                    "exclude_cash_only_tolls": False,
                    "top_speed": 140,
                    "fixed_speed": 0,
                    "toll_booth_penalty": 0,
                    "toll_booth_cost": 15,
                    "gate_penalty": 300,
                    "gate_cost": 30,
                    "include_hov2": False,
                    "include_hov3": False,
                    "include_hot": False,
                    "disable_hierarchy_pruning": False,
                }
            },
            "contours": [{"time": t} for t in contour_times],
            "locations": [{"lon": self.lon, "lat": self.lat, "type": "break"}],
            "units": "kilometers",
            "id": f"valhalla_isochrones_lonlat_{self.lon},{self.lat}_range_{self.max_time}_interval_{self.interval}",
        }
