import logging
from typing import Dict, List

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import Entity

from custom_components.auto_areas.auto_area import AutoArea
from custom_components.auto_areas.const import (
    CONFIG_SLEEPING_AREA,
    DOMAIN_DATA,
)
from custom_components.auto_areas.ha_helpers import get_data
from custom_components.auto_areas.sleep_mode_switch import SleepModeSwitch

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(
    hass: HomeAssistant,
    config,
    async_add_entities: AddEntitiesCallback,
    discovery_info=None,
):
    """Set up all switches"""
    _LOGGER.info("Setup switch platform %s", config)

    entities: List[Entity] = []
    auto_areas: Dict[AutoArea] = get_data(hass, DOMAIN_DATA)
    for area in auto_areas.values():
        if area.config.get(CONFIG_SLEEPING_AREA) is True:
            entities.append(SleepModeSwitch(hass, area))

    async_add_entities(entities)
