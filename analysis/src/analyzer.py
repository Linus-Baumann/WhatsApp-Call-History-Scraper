def calculate_total_duration(call_data):
    """
    Calculates the total duration of all calls.

    Args:
        call_data (list[dict]): List of call records.

    Returns:
        int: The total duration of all calls in minutes.
    """
    total_duration = sum(int(call["duration"]) for call in call_data)
    return total_duration
