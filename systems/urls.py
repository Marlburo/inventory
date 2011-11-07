from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail, object_list
from models import ServerModel, Location, Allocation, SystemRack, KeyValue

from misc.generic_views import create_object, update_object, delete_object, gen_mod_dict, gen_info_dict, gen_del_dict

urlpatterns = patterns('systems',
    (r'^quicksearch/$', 'views.system_quicksearch_ajax'),
    (r'^list_all_systems_ajax/$', 'views.list_all_systems_ajax'),
    (r'^get_network_adapters/(\d+)/$', 'views.get_network_adapters'),
    (r'^create_network_adapter/(\d+)/$', 'views.create_network_adapter'),
    (r'^get_expanded_key_value_store/(\d+)/$', 'views.get_expanded_key_value_store'),
    (r'^delete_network_adapter/(\d+)/(\d+)/$', 'views.delete_network_adapter'),
    (r'^save_network_adapter/(\d+)/$', 'views.save_network_adapter'),
    (r'^get_key_value_store/(\d+)/$', 'views.get_key_value_store'),
    (r'^create_key_value/(\d+)/$', 'views.create_key_value'),
    (r'^delete_key_value/(\d+)/(\d+)/$', 'views.delete_key_value'),
    (r'^save_key_value/(\d+)/$', 'views.save_key_value'),
    (r'^new/$', 'views.system_new'),
    (r'^show/(\d+)/$', 'views.system_show'),
    (r'^show/a(\d+)/$', 'views.system_show_by_asset_tag'),
    (r'^edit/(\d+)/$', 'views.system_edit'),
    (r'^delete/(\d+)/$', 'views.system_delete'),
    (r'^ajax_check_dupe_nic/(?P<system_id>\d+)/(?P<adapter_number>\d+)[/]$', 'views.check_dupe_nic'),
    (r'^ajax_check_dupe_nic_name/(?P<system_id>\d+)/(?P<adapter_name>.*)[/]$', 'views.check_dupe_nic_name'),
    url(r'^csv/$', 'views.system_csv', name="system-csv"),
    url(r'^releng_csv/$', 'views.system_releng_csv', name="system-csv"),
    url(r'^csv/import/$', 'views.csv_import', name='system-csv-import'),

    url(r'^racks/$', 'views.racks', name='system_rack-list'),
    url(r'^racks/delete/(?P<object_id>\d+)/$', delete_object, gen_del_dict(SystemRack, 'system_rack-list'), name='rack-delete'),
    url(r'^racks/new/$', create_object, gen_mod_dict(SystemRack, 'system_rack-list'), name="system_rack-new"),
    url(r'^racks/edit/(?P<object_id>\d+)/$', update_object, gen_mod_dict(SystemRack, 'system_rack-list'), name="system_rack-edit"),
    url(r'^racks/system/new/(?P<rack_id>\d+)/$', 'views.new_rack_system_ajax', name='racks-system-new'),
    
    url(r'^server_models/new/$', create_object, gen_mod_dict(ServerModel, 'server_model-list'), name="server_model-new"),
    url(r'^server_models/edit/(?P<object_id>\d+)/$', update_object, gen_mod_dict(ServerModel, 'server_model-list'), name="server_model-edit"),
    url(r'^server_models/$', object_list, gen_info_dict(ServerModel), name="server_model-list"),
    url(r'^server_models/show/(?P<object_id>\d+)/$', object_detail, gen_info_dict(ServerModel), name="server_model-show"),
    #url(r'^server_models/delete/(?P<object_id>\d+)/$', delete_object, gen_del_dict(ServerModel, 'server_model-list'), name='server_model-delete'),

    url(r'^locations/new/$', create_object, gen_mod_dict(Location, 'location-list'), name="location-new"),
    url(r'^locations/edit/(?P<object_id>\d+)/$', update_object, gen_mod_dict(Location, 'location-list'), name="location-edit"),
    url(r'^locations/$', object_list, gen_info_dict(Location), name="location-list"),
    url(r'^locations/show/(?P<object_id>\d+)/$', object_detail, gen_info_dict(Location), name="location-show"),
    #url(r'^locations/delete/(?P<object_id>\d+)/$', delete_object, gen_del_dict(Location, 'location-list'), name='location-delete'),

    url(r'^allocations/new/$', create_object, gen_mod_dict(Allocation, 'allocation-list'), name="allocation-new"),
    url(r'^allocations/edit/(?P<object_id>\d+)/$', update_object, gen_mod_dict(Allocation, 'allocation-list'), name="allocation-edit"),
    url(r'^allocations/$', object_list, gen_info_dict(Allocation), name="allocation-list"),
    url(r'^allocations/show/(?P<object_id>\d+)/$', object_detail, gen_info_dict(Allocation), name="allocation-show"),
    #url(r'^allocations/delete/(?P<object_id>\d+)/$', delete_object, gen_del_dict(Allocation, 'allocation-list'), name='allocation-delete'),
)