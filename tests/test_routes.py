"""Each parametrized example exercises a different production call site."""

import pytest

from route_window import demand, stops, timing, zones
from route_window.overview import summarize


@pytest.mark.parametrize(("report", "args", "expected"), [
    (stops.path_count, (["A", "B", "A"],), 6),
    (stops.adjacent_pairs, (["A", "B", "C"],), [("A", "B"), ("B", "C")]),
    (stops.loops, ("ABA",), [("A", "B", "A")]),
    (stops.from_origin, ("ABA", "B"), [("B",), ("B", "A")]),
    (stops.non_repeating, ("AA",), [("A",), ("A",)]),
    (stops.direct_paths, ("ABC", "A", "C"), [("A", "B", "C")]),
    (timing.total_durations, ([2, 3, 1],), [2, 3, 1, 5, 4, 6]),
    (timing.under_budget, ([2, 5, 1], 3), [(2,), (1,)]),
    (timing.exact_duration, ([2, 3, 5], 5), [(5,), (2, 3)]),
    (timing.longest_within, ([2, 2, 1], 3), 2),
    (timing.slow_pairs, ([3, 5, 4], 9), [(5, 4)]),
    (timing.even_pace, ([3, 3, 2],), [(3, 3)]),
    (demand.peak_total, ([2, 1, 4],), 7),
    (demand.empty_runs, ([0, 0, 1],), [(0,), (0,), (0, 0)]),
    (demand.full_runs, ([4, 5, 2], 4), [(4,), (5,), (4, 5)]),
    (demand.growing, ([1, 3, 2],), [(1, 3)]),
    (demand.single_spikes, ([2, 8, 7], 7), [(8,), (7,), (2, 8)]),
    (demand.busiest_pair, ([1, 4, 6],), (4, 6)),
    (zones.flat_fare, ("ABB",), [("A",), ("B",), ("B",), ("B", "B")]),
    (zones.crossings, ("AAB",), [("A", "B")]),
    (zones.touches, ("ABC", "B"), [("B",), ("A", "B"), ("B", "C"), ("A", "B", "C")]),
    (zones.avoids, ("ABA", "A"), [("B",)]),
    (zones.distinct_paths, ("AA",), [("A",), ("A", "A")]),
    (zones.through_zones, ("ABA", 2), [("A", "B"), ("B", "A"), ("A", "B", "A")]),
], ids=lambda value: getattr(value, "__name__", None))
def test_report(report, args, expected):
    assert report(*args) == expected


def test_overview():
    assert summarize(["A", "B", "A"]) == {
        "first": "A", "last": "A", "visits": 3, "preview": ["A", "B", "A"],
        "third": "A", "distinct": ["A", "B"], "pairs": [("A", "B"), ("B", "A")],
        "display_slots": ["A", "B", "A"], "named_stops": 3,
    }


def test_empty_overview():
    assert summarize([]) == {
        "first": None, "last": None, "visits": 0, "preview": [], "third": None,
        "distinct": [], "pairs": [], "display_slots": ["-", "-", "-"], "named_stops": 0,
    }
