def tip_amount(subtotal, pct):
    """Return the tip: `pct` percent of `subtotal`, rounded to the nearest cent.

    >>> tip_amount(50, 20)
    10.0
    """
    tip = subtotal * (pct / 100)
    return round(tip, 2)

def grand_total(subtotal, pct):
    """Return the subtotal plus the tip, rounded to the nearest cent.
    Hint: you can call tip_amount() from here.

    >>> grand_total(50, 20)
    60.0
    """
    sum_total = subtotal + tip_amount(subtotal, pct)
    return round(sum_total, 2)

def split_evenly(total, people):
    """Return each person's share of `total`, rounded to the nearest cent.

    Must raise ValueError if `people` is not greater than 0.

    >>> split_evenly(60, 4)
    15.0
    """
    if people <= 0:
        raise ValueError("Invalid. Number of guests must be greater than ")

    split = total / people
    return round(split, 2)

def is_generous(pct):
    """Return True when a tip percent is considered generous (20% or more).

    >>> is_generous(20)
    True
    """
    if pct >= 20:
        return True
    else: 
        return False
    