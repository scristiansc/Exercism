"""Prevent a nuclear meltdown."""

MAX_TEMPERATURE_IN_CRITICALITY = 800
MIN_NEUTRONS_EMITTED_IN_CRITICALITY = 500
MAX_TEMPERATURE_PRODUCT_IN_CRITICALITY = 500_000


def is_criticality_balanced(temperature, neutrons_emitted):
    """
    :param temperature: temperature value in kelvin.
    :param neutrons_emitted: number of neutrons emitted per second.
    :return: bool - is criticality balanced?
    A reactor is said to be critical if it satisfies the following conditions:
    -The temperature is less than 800 K.
    -The number of neutrons emitted per second is greater than 500.
    -The product of temperature and neutrons emitted per second is < 500000.
    """
    return (
        temperature < MAX_TEMPERATURE_IN_CRITICALITY and
        neutrons_emitted > MIN_NEUTRONS_EMITTED_IN_CRITICALITY and
        temperature * neutrons_emitted < MAX_TEMPERATURE_PRODUCT_IN_CRITICALITY
        )


def reactor_efficiency(voltage, current, theoretical_max_power):
    """
    :param voltage: voltage value.
    :param current: current value.
    :param theoretical_max_power: power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return "green"
    if efficiency >= 60:
        return "orange"
    if efficiency >= 30:
        return "red"

    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """"
    :param temperature: value of the temperature in kelvin.
    :param neutrons_produced_per_second: neutron flux.
    :param threshold: threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1.'LOW' `temperature * neutrons per second` < 90% of `threshold`
    2.'NORMAL' `temperature * neutrons per second` +/- 10% of `threshold`
    3.'DANGER' `temperature * neutrons per second` isn't in the ranges above.
    """
    result = temperature * neutrons_produced_per_second
    threshold_upper_bound = threshold * 1.1
    threshold_lower_bound = threshold * 0.9

    if result < threshold_lower_bound:
        return "LOW"
    if threshold_lower_bound <= result <= threshold_upper_bound:
        return "NORMAL"

    return "DANGER"
