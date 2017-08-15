from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = 'bcpp_community'
    mapper_model = 'plot.plot'


if settings.APP_NAME == 'bcpp_community':

    from edc_device.device_permission import DevicePermissions
    from edc_device.device_permission import DeviceAddPermission, DeviceChangePermission
    from edc_device.constants import CENTRAL_SERVER, CLIENT, NODE_SERVER
    from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
    from edc_map.apps import AppConfig as BaseEdcMapAppConfig

    class EdcMapAppConfig(BaseEdcMapAppConfig):
        verbose_name = 'Test Mappers'
        mapper_model = 'plot.plot'
        landmark_model = []
        verify_point_on_save = False
        zoom_levels = ['14', '15', '16', '17', '18']
        identifier_field_attr = 'plot_identifier'
        extra_filter_field_attr = 'enrolled'

    class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
        use_settings = True
        device_permissions = DevicePermissions(
            DeviceAddPermission(
                model='plot.plot',
                device_roles=[CENTRAL_SERVER, CLIENT]),
            DeviceChangePermission(
                model='plot.plot',
                device_roles=[NODE_SERVER, CENTRAL_SERVER, CLIENT]))
