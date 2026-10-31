import pytest

from daycare_fees import enrolment_allowed, extra_hours_fee, pickup_status


@pytest.mark.parametrize(
    ("age_group", "hours", "has_sibling", "expected"),
    [
        ("infant", 20, False, 0),
        ("infant", 20, True, 0),
        ("toddler", 30, False, 45),
        ("toddler", 31, True, 9),
        ("infant", 41, False, 462),
        ("preschool", 56, True, 294),
    ],
)
def test_extra_hours_covers_fee_branches(
    age_group, hours, has_sibling, expected
):
    assert extra_hours_fee(age_group, hours, has_sibling) == expected


@pytest.mark.parametrize(
    ("age_group", "hours", "message"),
    [
        ("school_age", 10, "unknown age group"),
        ("infant", -1, "invalid hours"),
    ],
)
def test_extra_hours_covers_validation_branches(age_group, hours, message):
    with pytest.raises(ValueError, match=message):
        extra_hours_fee(age_group, hours, False)


@pytest.mark.parametrize(
    ("age_months", "vacancies", "pending", "expected"),
    [
        (12, 0, True, True),
        (11, 0, True, False),
        (5, 1, False, False),
        (6, 0, False, False),
        (6, 1, False, True),
    ],
)
def test_enrolment_covers_all_decision_branches(
    age_months, vacancies, pending, expected
):
    assert enrolment_allowed(age_months, vacancies, pending) is expected


@pytest.mark.parametrize(
    ("minutes_left", "is_aftercare", "is_friday", "expected"),
    [
        (20, True, False, "on_time"),
        (30, False, True, "on_time"),
        (5, False, False, "late"),
        (15, True, True, "late"),
        (-1, False, True, "overdue"),
    ],
)
def test_pickup_covers_cutoff_and_status_branches(
    minutes_left, is_aftercare, is_friday, expected
):
    assert pickup_status(minutes_left, is_aftercare, is_friday) == expected
