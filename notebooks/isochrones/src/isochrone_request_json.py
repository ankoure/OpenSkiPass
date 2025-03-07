def create_isochrone_request(lon, lat, contour_times,max_time,interval):
    return {"polygons": True,
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
            "disable_hierarchy_pruning": False
        }
    },
    "contours": [{"time": t} for t in contour_times],
    "locations": [
        {
            "lon": lon,
            "lat": lat,
            "type": "break"
        }
    ],
    "units": "kilometers",
    "id": f"valhalla_isochrones_lonlat_{lon},{lat}_range_{max_time}_interval_{interval}"}
