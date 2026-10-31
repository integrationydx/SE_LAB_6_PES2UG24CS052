import pytest

from daycare_fees import enrolment_allowed, extra_hours_fee, pickup_status


def test_extra_hours_rejects_unknown_age_group():
    with pytest.raises(ValueError, match="unknown age group"):
        extra_hours_fee("school_age", 10, False)


def test_extra_hours_rejects_negative_hours():
    with pytest.raises(ValueError, match="invalid hours"):
        extra_hours_fee("infant", -1, False)


def test_infant_extra_hours_uses_high_rate():
    assert extra_hours_fee("infant", 45, False) == 550


def test_toddler_sibling_hours_use_extra_included_hours():
    assert extra_hours_fee("toddler", 31, True) == 9


def test_hours_within_included_allowance_have_no_fee():
    assert extra_hours_fee("preschool", 30, False) == 0


def test_enrolment_pending_immunisation_allows_old_enough_child():
    assert enrolment_allowed(12, 0, True) is True


def test_enrolment_rejects_child_under_six_months():
    assert enrolment_allowed(5, 1, False) is False


def test_enrolment_requires_a_vacancy():
    assert enrolment_allowed(24, 0, False) is False


def test_pickup_statuses():
    assert pickup_status(20, True, False) == "on_time"
    assert pickup_status(5, False, False) == "late"
    assert pickup_status(-6, False, False) == "overdue"
    assert pickup_status(30, False, True) == "on_time"
