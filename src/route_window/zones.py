"""Fare-zone sequences for reporting on transfers and boundary crossings."""

import more_itertools


def flat_fare(zones):
    return [part for part in more_itertools.substrings(zones) if len(set(part)) == 1]


def crossings(fare_zones):
    return [part for part in more_itertools.substrings(fare_zones)
            if len(part) == 2 and part[0] != part[1]]


def touches(service_zones, zone):
    return [part for part in more_itertools.substrings(service_zones) if zone in part]


def avoids(zone_ids, excluded):
    return [part for part in more_itertools.substrings(zone_ids)
            if excluded not in part]


def distinct_paths(zone_sequence):
    return list(dict.fromkeys(more_itertools.substrings(zone_sequence)))


def through_zones(corridor, count):
    return [part for part in more_itertools.substrings(corridor)
            if len(set(part)) == count]
