"""Route summary using nine other public more-itertools operations."""

import more_itertools as mi


def summarize(stops):
    return {
        "first": mi.first(stops, None),
        "last": mi.last(stops, None),
        "visits": mi.ilen(stops),
        "preview": mi.take(3, stops),
        "third": mi.nth(stops, 2),
        "distinct": list(mi.unique_everseen(stops)),
        "pairs": list(mi.windowed(stops, 2)) if len(stops) >= 2 else [],
        "display_slots": list(mi.padded(stops[:3], "-", 3)),
        "named_stops": mi.quantify(stops, bool),
    }
