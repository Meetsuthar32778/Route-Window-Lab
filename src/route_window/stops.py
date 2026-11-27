"""Reports over ordered stop codes, including repeat visits on circular routes."""

import more_itertools as mi


def path_count(stops):
    return sum(1 for _ in mi.substrings(stops))


def adjacent_pairs(itinerary):
    return [part for part in mi.substrings(itinerary) if len(part) == 2]


def loops(stop_codes):
    return [part for part in mi.substrings(stop_codes)
            if len(part) > 1 and part[0] == part[-1]]


def from_origin(route, origin):
    return [part for part in mi.substrings(route) if part[0] == origin]


def non_repeating(trip):
    return [part for part in mi.substrings(trip)
            if len(set(part)) == len(part)]


def direct_paths(journey, start, end):
    return [part for part in mi.substrings(journey)
            if part[0] == start and part[-1] == end]
