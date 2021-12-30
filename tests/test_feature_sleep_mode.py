from functools import partial
import logging

import pytest_bdd
from pytest_bdd import scenario

_LOGGER = logging.getLogger(__name__)

scenario = partial(pytest_bdd.scenario, "features/sleep_mode.feature")


@scenario("Lights are controlled automatically with sleep mode turned off")
def test_lights_behave_normally_without_sleep_mode():
    pass


# @scenario("Lights stay off during sleep mode")
# def test_lights_stay_off_with_sleep_mode():
#     pass
