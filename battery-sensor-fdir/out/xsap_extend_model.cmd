set on_failure_script_quits
read_model -i "battery_sensor_fdir.smv"
flatten_hierarchy
fe_load_doc -o "out/errors.log"  -p "/home/devtool/FBK_Tools/xSAP-1.5.0/xSAP/data/schema" -i "out/expanded_battery_sensor_fdir.xml"
fe_extend_module -m "out/fms_battery_sensor_fdir.xml"   -o "out/extended_battery_sensor_fdir.smv"
quit
