"""Travel-time windows. Durations and thresholds are expressed in minutes."""

from more_itertools import substrings


def total_durations(minutes):
    return [sum(part) for part in substrings(minutes)]


def under_budget(durations, budget):
    return [part for part in substrings(durations) if sum(part) <= budget]


def exact_duration(legs, target):
    return [part for part in substrings(legs) if sum(part) == target]


def longest_within(times, limit):
    return max((len(part) for part in substrings(times) if sum(part) <= limit), default=0)


def slow_pairs(travel_times, threshold):
    return [part for part in substrings(travel_times)
            if len(part) == 2 and sum(part) >= threshold]


def even_pace(samples):
    return [part for part in substrings(samples)
            if len(part) > 1 and min(part) == max(part)]
