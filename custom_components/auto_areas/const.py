"""Constants"""
from homeassistant.components.binary_sensor import (
    DEVICE_CLASS_MOTION,
    DEVICE_CLASS_OCCUPANCY,
    DEVICE_CLASS_PRESENCE,
)
from homeassistant.components.binary_sensor import DOMAIN as BINARY_SENSOR_DOMAIN
from homeassistant.components.light import DOMAIN as LIGHT_DOMAIN

# from homeassistant.components.media_player import DOMAIN as MEDIA_PLAYER_DOMAIN
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.components.switch import DOMAIN as SWITCH_DOMAIN
from homeassistant.const import STATE_HOME, STATE_ON, STATE_PLAYING

import voluptuous as vol
from voluptuous.schema_builder import PREVENT_EXTRA

NAME = "Auto Areas"
DOMAIN = "auto_areas"
DOMAIN_DATA = f"{DOMAIN}_data"

# Prefixes for created entities (area name is appended: f"{ENTITY_NAME_FOO{area.name}")
ENTITY_FRIENDLY_NAME_AREA_PRESENCE = "Area Presence "
ENTITY_NAME_AREA_PRESENCE = "binary_sensor.area_presence_"

ENTITY_FRIENDLY_NAME_AREA_PRESENCE_LOCK = "Area Presence Lock "
ENTITY_NAME_AREA_PRESENCE_LOCK = "switch.area_presence_lock_"

ENTITY_FRIENDLY_NAME_AREA_SLEEP_MODE = "Area Sleep Mode "
ENTITY_NAME_AREA_SLEEP_MODE = "switch.area_sleep_mode_"

# Area Config options
CONFIG_SLEEPING_AREA = "is_sleeping_area"
CONFIG_MOTION_LIGHTS = "enable_motion_lights"

CONFIG_OPTIONS = {
    CONFIG_SLEEPING_AREA: False,
    CONFIG_MOTION_LIGHTS: False
}

OPTIONS_SCHEMA = {
    vol.Optional(
        option,
        default=default
    ): type(default)
    for option, default in CONFIG_OPTIONS.items()
}

CONFIG_SCHEMA = vol.Schema(
    {
        vol.Optional(CONFIG_SLEEPING_AREA, default=False): bool,
        vol.Optional(CONFIG_MOTION_LIGHTS, default=False): bool,
        str: vol.Any(OPTIONS_SCHEMA, None)
    }
)

# Entity gathering configuration
AUTO_AREAS_RELEVANT_DOMAINS = [
    BINARY_SENSOR_DOMAIN,
    SENSOR_DOMAIN,
    SWITCH_DOMAIN,
    LIGHT_DOMAIN,
]

# Presence entities
PRESENCE_BINARY_SENSOR_DEVICE_CLASSES = (
    DEVICE_CLASS_MOTION,
    DEVICE_CLASS_OCCUPANCY,
    DEVICE_CLASS_PRESENCE,
)

PRESENCE_ON_STATES = [
    STATE_ON,
    STATE_HOME,
    STATE_PLAYING,
]
