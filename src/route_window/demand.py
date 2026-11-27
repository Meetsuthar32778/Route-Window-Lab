"""Passenger counts across consecutive segments."""

from more_itertools import substrings as segments


def peak_total(boardings):
    return max((sum(part) for part in segments(boardings)), default=0)


def empty_runs(counts):
    return [part for part in segments(counts) if not any(part)]


def full_runs(loads, capacity):
    return [part for part in segments(loads) if min(part) >= capacity]


def growing(ridership):
    return [part for part in segments(ridership)
            if len(part) > 1 and all(a < b for a, b in zip(part, part[1:]))]


def single_spikes(passengers, threshold):
    return [part for part in segments(passengers)
            if sum(value >= threshold for value in part) == 1]


def busiest_pair(occupancies):
    pairs = (part for part in segments(occupancies) if len(part) == 2)
    return max(pairs, key=sum, default=())
