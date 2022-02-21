"""AutoAreas custom_component for Home Assistant"""
import logging
from typing import MutableMapping

from homeassistant.components.binary_sensor import DOMAIN as BINARY_SENSOR_DOMAIN
from homeassistant.components.switch import DOMAIN as SWITCH_DOMAIN
from homeassistant.core import HomeAssistant
from homeassistant.helpers import discovery
from homeassistant.helpers.area_registry import AreaRegistry
from homeassistant.helpers.typing import ConfigType

from custom_components.auto_areas.auto_area import AutoArea
from custom_components.auto_areas.ha_helpers import set_data

from voluptuous.error import MultipleInvalid

from .const import DOMAIN, DOMAIN_DATA, CONFIG_SCHEMA, CONFIG_OPTIONS

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Setup integration (YAML-based)"""

    # Load and validate config
    auto_areas_config: dict = config.get(DOMAIN) or {}
    try:
        CONFIG_SCHEMA(auto_areas_config)
    except MultipleInvalid as exception:
        _LOGGER.error(
            "Configuration is invalid (validation message: '%s'). Config: %s",
            exception.error_message,
            auto_areas_config,
        )
        return False

    _LOGGER.debug("Found config %s", auto_areas_config)

    area_registry: AreaRegistry = await hass.helpers.area_registry.async_get_registry()

    auto_areas: MutableMapping[str, AutoArea] = {}

    for area in area_registry.async_list_areas():
        area_config = config.get(area.normalized_name, None)

        if area_config is None:
            area_config = {
                option: config.get(option) for option in CONFIG_OPTIONS.keys()
            }

        auto_areas[area.id] = AutoArea(hass, area, area_config)

    set_data(hass, DOMAIN_DATA, auto_areas)

    hass.async_create_task(
        discovery.async_load_platform(
            hass,
            component=BINARY_SENSOR_DOMAIN,  # un-intuitive but correct
            platform=DOMAIN,
            discovered={},
            hass_config={"nonempty": "dict"},  # should not be an empty dict
        )
    )

    hass.async_create_task(
        discovery.async_load_platform(
            hass,
            component=SWITCH_DOMAIN,
            platform=DOMAIN,
            discovered={},
            hass_config={"nonempty": "dict"},
        )
    )

    return True


async def async_setup_entry(hass, config_entry, async_add_devices):
    return


async def async_unload_entry(hass, entry):
    return
