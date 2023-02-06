import obspython as obs
from pymem import Pymem
from pymem.ptypes import RemotePointer

process_name = ""
pointer = 0
offset = 0
address = 0
interval = 1
source_name = ""
pm = Pymem


def getPointerAddress(base, offsets):
    global pm
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


def update_text():
    global process_name, pointer, offset, source_name, address
    source = obs.obs_get_source_by_name(source_name)
    if source is not None:
        try:
            text = str(pm.read_int(address))
        except Exception:
            pass
        else:
            settings = obs.obs_data_create()
            obs.obs_data_set_string(settings, "text", text)
            obs.obs_source_update(source, settings)

            obs.obs_source_release(source)


def attach(props, prop):
    global process_name, pointer, offset, source_name, interval, address, pm
    obs.timer_remove(update_text)
    if process_name:
        pm = Pymem(process_name)
        address = getPointerAddress(pm.base_address + pointer, offsets=[offset])

        obs.timer_add(update_text, interval * 1000)


def script_description():
    return "Display Deaths in Elden Ring\nby Kam1k4dze"


def script_defaults(settings):
    obs.obs_data_set_default_string(settings, "procces_name", "eldenring.exe")
    obs.obs_data_set_default_string(settings, "pointer", "03CD1948")
    obs.obs_data_set_default_string(settings, "offset", "94")
    obs.obs_data_set_default_int(settings, "interval", 5)


def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_text(props, "procces_name", "Procces name", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "pointer", "Pointer(hex)", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "offset", "Offset(hex)", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_int(props, "interval", "Interval(sec)", 1, 3600, 1)
    obs.obs_properties_add_button(props, "button", "Attach", attach)
    source_id = obs.obs_get_source_by_name(source_name)
    p = obs.obs_properties_add_list(props, "source", "Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)
    sources = obs.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = obs.obs_source_get_unversioned_id(source)
            if source_id == "text_gdiplus" or source_id == "text_ft2_source":
                name = obs.obs_source_get_name(source)
                obs.obs_property_list_add_string(p, name, name)

        obs.source_list_release(sources)
    return props


def script_update(settings):
    global process_name, pointer, offset, source_name, interval
    process_name = obs.obs_data_get_string(settings, "procces_name")
    pointer = int(obs.obs_data_get_string(settings, "pointer"), 16)
    offset = int(obs.obs_data_get_string(settings, "offset"), 16)
    source_name = obs.obs_data_get_string(settings, "source")
    interval = obs.obs_data_get_int(settings, "interval")
